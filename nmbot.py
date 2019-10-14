import requests
import os
import json
import logging
from random import uniform
from time import sleep


# TO DO
# gold gain from world grinding
# legendary weapon grinding






with open('headers.json', 'r') as file:
    HEADERS = json.load(file)

with open('cookies.json', 'r') as file:
    COOKIES = json.load(file)

WORLD_MISSION_URL = 'https://www.ninjamanager.com/world/area/anbu-hideout/mission/6'



# EXCEPTIONS
class OutOfEnergy(Exception):
    pass





class NMBot():
    def __init__():
        self.session = requests.Session()

        self.arena_energy = True
        self.world_energy = True

        self.arena_successes = 0
        self.arena_losses = 0
        self.arena_rating = 0

        self.world_successes = 0
        self.world_losses = 0
        self.item_successes = 0

        if os.path.exists('log.txt'): # don't append to the last log
            os.remove('log.txt')
        self.logger = open('log.txt', 'a+')



    def execute():
        # maion logic
        loop_count = 1

        try:
            while True:
                self.check_energy()

                if arena_energy or world_energy:
                    self.log('LOOP #' + loop_count + '\n')

                    if arena_energy:
                        self.log('ARENA')
                        self.arena_actions()
                        self.log('\n')
                        sleep(rng(300, 600)) # 5 to 10 minutes
                    else:
                        self.log('ARENA out of energy' + '\n')

                    if world_energy:
                        self.log('WORLD')
                        self.world_actions()
                        self.log('\n')
                        sleep(rng(300, 600)) # 5 to 10 minutes
                    else:
                        self.log('WORLD out of energy')

                    self.log('\n\n\n')
                    loop_count += 1
                else:
                    sleep(rng(1200, 1800)) # 20 to 30 minutes
        except Exception as e:
            self.log(e)
            self.logger.close()
            with open('summary.txt', 'w+') as file:
                file.write('Total Loops:  ' + loop_count + '\n' +
                         '\nArena Wins:   ' + self.arena_successes +
                         '\nArena Losses: ' + self.arena_losses +
                         '\nRating Delta: ' + self.arena_rating + '\n' +
                         '\nWorld Wins:   ' + self.world_successes +
                         '\nWorld Losses: ' + self.world_losses +
                         '\nItems Gained: ' + self.item_successes)





    # ARENA
    def arena_actions():
        # all the things we want to do in the arena screen
        try:
            challengers = self.get_challengers()
            for team in challengers:
                sleep(rng(0.5, 3))
                self.challenge(team)
            self.log('finished challenging teams')
        except FileNotFoundError:
            self.log('ERROR READING FROM response.txt')
        except OutOfEnergy:
            self.log('OUT OF ARENA ENERGY')



    def get_challengers() -> set(str):
        # gets a list of rematch challengers
        raw = self.session.get('http://www.ninjamanager.com/arena', headers=HEADERS, cookies=COOKIES)
        challengers = set()

        with open('response.txt', 'w+', encoding='utf-8') as file:
            file.write(raw.text)

        with open('response.txt', 'r') as file:
            for line in file:
                if '-icon-challenge-return' in line:
                    challengers.add(line[line.find('data-teamid="')+13 : line.find('">')])

        os.remove('response.txt')
        return challengers



    def challenge(team_id: str):
        # challenges a team
        response = self.session.post('http://www.ninjamanager.com/ajax/challengeTeam', headers=HEADERS, cookies=COOKIES, data={'TeamID': team_id,'SkipBattle': 'true'})

        if 'Not enough energy!' in response.text:
            raise OutOfEnergy

        info = json.load(response.text)

        self.log('challenged team ' + team_id)

        if '-result-win' in info['challengeBox']:
            self.arena_successes += 1
            self.log('arena won')
        elif '-result-loss' in info['challengeBox']:
            self.arena_losses += 1
            self.log('arena lost')

        self.arena_rating += int(info['mission']['ChallengeBox']['Rating'])
        self.log('rating gain = ' + info['mission']['ChallengeBox']['Rating'])





    # WORLD
    def world_actions():
        # all the things we want to do in the world screen
        try:
            info = self.do_mission(WORLD_MISSION_URL)
            self.log('finished world mission(s)')
        except OutOfEnergy:
            self.log('OUT OF WORLD ENERGY')



    def do_mission(url: str):
        # executes world mission
        response = self.session.get(url, headers=HEADERS, cookies=COOKIES)

        if 'Not enough world energy!' in response.text:
            raise OutOfEnergy

        info = json.load(response.text)

        if r'pm-battle-matchup__title\">Defeat<\/div>' in info['content']:
            self.world_successes += 1
            self.log('world won')
        elif r'pm-battle-matchup__title\">Victory<\/div>' in info['content']
            self.world_losses += 1
            self.log('world lost')

        if ['mission']['Material']['Rolls'][0]['Roll']['Success']:
            self.item_successes += 1
            self.log('Item Get')
        else:
            self.log('No Item')





    # GENERAL
    def check_energy():
        # checks how much energy we have
        response = self.session.get('http://www.ninjamanager.com')
        raw = response.text

        arena_energy_raw = raw[raw.find('js-header-energy-arena'):]
        world_energy_raw = raw[raw.find('js-header-energy-world'):]

        arena_energy_value = int(arena_energy_raw[arena_energy_raw.find('cur">')+5 : arena_energy_raw.find('</span>')])
        world_energy_value = int(world_energy_raw[world_energy_raw.find('cur">')+5 : world_energy_raw.find('</span>')])

        if arena_energy_value < 4:
            self.arena_energy = False
        else:
            self.arena_energy = True

        if world_energy_value < 7:
            self.world_energy = False
        else:
            self.world_energy = True



    def log(msg: str):
        # prints to console and file
        print(msg)
        self.logger.write('\n' + msg)





def rng(start: float, stop:float) -> float:
    return uniform(start, stop)





if __name__ == "__main__":
    bot = NMBot()
    bot.execute()