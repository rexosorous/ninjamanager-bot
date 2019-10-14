import requests
import os
import json
import traceback
from random import uniform
from time import sleep


# TO DO
# MIGREATE TO SELENIUM
# gold gain from world grinding
# legendary weapon grinding





WORLD_MISSION_URL = 'https://www.ninjamanager.com/world/area/anbu-hideout/mission/6'



# EXCEPTIONS
class OutOfEnergy(Exception):
    pass

class MaxChallenges(Exception):
    pass





class NMBot():
    def __init__(self, headers, cookies):
        self.session = requests.Session()

        self.headers = headers
        self.cookies = cookies

        self.arena_energy = True
        self.world_energy = True

        self.team_blacklist = {'965'} # 965 = my own team

        self.arena_successes = 0
        self.arena_losses = 0

        self.world_successes = 0
        self.world_losses = 0
        self.item_successes = 0

        if os.path.exists('log.txt'): # don't append to the last log
            os.remove('log.txt')
        self.logger = open('log.txt', 'a+')



    def execute(self):
        # maion logic
        loop_count = 0

        try:
            while True:
                self.check_energy()

                if loop_count % 5 == 0:
                    self.team_blacklist = {'965'}

                if self.arena_energy or self.world_energy:
                    self.log('LOOP #' + str(loop_count) + '\n')

                    # if self.arena_energy:
                    #     self.arena_actions()
                    #     self.log('\n')
                    #     sleep(rng(300, 600)) # 5 to 10 minutes
                    # else:
                    #     self.log('ARENA out of energy' + '\n')

                    if self.world_energy:
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
            self.log('\n\n\n\n\n\n')
            self.log('%s' % e)
            self.log(traceback.format_exc())
            self.logger.close()
            with open('summary.txt', 'w+') as file:
                file.write('Total Loops:  ' + str(loop_count) + '\n' +
                         '\nArena Wins:   ' + str(self.arena_successes) +
                         '\nArena Losses: ' + str(self.arena_losses) +
                         '\nWorld Wins:   ' + str(self.world_successes) +
                         '\nWorld Losses: ' + str(self.world_losses) +
                         '\nItems Gained: ' + str(self.item_successes))





    # ARENA
    def arena_actions(self):
        # all the things we want to do in the arena screen
        try:
            challengers = self.get_challengers()
            for team in challengers:
                sleep(rng(1, 3))
                self.challenge(team)
        except FileNotFoundError:
            self.log('ERROR READING FROM response.txt')
        except OutOfEnergy:
            self.log('OUT OF ARENA ENERGY')



    def get_challengers(self) -> {str}:
        # gets a list of rematch challengers
        raw = self.session.get('https://www.ninjamanager.com/arena', headers=self.headers, cookies=self.cookies)
        challengers = set()

        with open('response.txt', 'w+', encoding='utf-8') as file:
            file.write(raw.text)

        with open('response.txt', 'r') as file:
            for line in file:
                if '-icon-challenge-return' in line:
                    team_id = line[line.find('data-teamid="')+13 : line.find('">')]
                    if team_id not in self.team_blacklist:
                        challengers.add(team_id)

        os.remove('response.txt')
        return challengers



    def challenge(self, team_id: str):
        # challenges a team
        response = self.session.post('https://www.ninjamanager.com/ajax/challengeTeam', headers=self.headers, cookies=self.cookies, data={'TeamID': team_id, 'SkipBattle': 'true'})

        if 'Not enough energy!' in response.text:
            raise OutOfEnergy

        if 'You have reached your max amount of recent challenges' in response.text:
            self.team_blacklist.add(team_id)
            raise MaxChallenges

        with open('arena_debug.txt', 'w+') as file:
            file.write(response.text)

        info = response.json()

        if '-result-win' in info['challengeBox']:
            self.arena_successes += 1
            self.log('won  against team ' + team_id)
        elif '-result-loss' in info['challengeBox']:
            self.arena_losses += 1
            self.log('lost against team ' + team_id)





    # WORLD
    def world_actions(self):
        # all the things we want to do in the world screen
        try:
            info = self.do_mission(WORLD_MISSION_URL)
        except OutOfEnergy:
            self.log('OUT OF WORLD ENERGY')



    def do_mission(self, url: str):
        # executes world mission
        response = self.session.get(url, headers=self.headers, cookies=self.cookies)

        if 'Not enough world energy!' in response.text:
            raise OutOfEnergy

        with open('world_debug.txt', 'w+') as file:
            file.write(response.text)

        info = response.json()

        if r'pm-battle-matchup__title\">Defeat<\/div>' in info['content']:
            self.world_successes += 1
            self.log('world won')
        elif r'pm-battle-matchup__title\">Victory<\/div>' in info['content']:
            self.world_losses += 1
            self.log('world lost')

        if ['mission']['Material']['Rolls'][0]['Roll']['Success']:
            self.item_successes += 1
            self.log('Item Get')
        else:
            self.log('No Item')





    # GENERAL
    def check_energy(self):
        # checks how much energy we have
        response = self.session.get('https://www.ninjamanager.com', headers=self.headers, cookies=self.cookies)
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



    def log(self, msg: str):
        # prints to console and file
        print(msg)
        self.logger.write('\n' + msg)





def rng(start: float, stop:float) -> float:
    # returns a random float between start and stop
    return uniform(start, stop)



# def save_and_load(text):
#     # saves and the immediately loads a json file because json.load() is funny
#     with open('response.json', 'w+', encoding='utf-8') as file:
#         file.write(text)

#     with open('response.json', 'r', encoding='utf-8') as file:
#         info = json.load(file)

#     return info



if __name__ == "__main__":
    with open('headers.json', 'r') as file:
        headers = json.load(file)

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    bot = NMBot(headers, cookies)
    bot.execute()