from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import json
import traceback
from random import uniform
from time import sleep


# TO DO
# add assert statements ot insure we are on the right page
# gold gain from world grinding
# legendary weapon grinding


# EXCEPTIONS
class OutOfEnergy(Exception):
    pass

class MaxChallenges(Exception):
    pass





class NMBot():
    def __init__(self, headers, cookies):
        self.bot = webdriver.Chrome()
        self.bot.get('https://www.ninjamanager.com')

        for ck in cookies:
            self.bot.add_cookie(ck)

        self.arena_energy = True
        self.world_energy = True

        self.team_blacklist = {'965'} # 965 = my own team

        self.arena_battles = 0
        self.world_successes = 0
        self.world_losses = 0
        self.item_successes = 0

        if os.path.exists('log.txt'): # don't append to the last log
            os.remove('log.txt')
        self.logger = open('log.txt', 'a+')



    def execute(self):
        # main logic
        loop_count = 0
        sleep(rng(2, 4))
        self.bot.refresh()
        sleep(rng(2.5, 6))

        try:
            while True:
                self.check_energy()

                if self.arena_energy or self.world_energy:
                    self.log('LOOP #' + str(loop_count) + '\n')

                    if self.arena_energy:
                        self.arena_actions()
                        self.log('\n')
                        sleep(rng(300, 600)) # 5 to 10 minutes
                    else:
                        self.log('ARENA out of energy' + '\n')

                    if self.world_energy:
                        self.world_actions()
                        self.log('\n')
                    else:
                        self.log('WORLD out of energy')

                    self.log('\n\n\n\n\n\n')
                    loop_count += 1

                sleep(rng(1200, 1800)) # 20 to 30 minutes


        except Exception as e:
            self.log('\n\n\n\n\n\n')
            self.log('%s' % e)
            self.log(traceback.format_exc())
            self.logger.close()
            with open('summary.txt', 'w+') as file:
                file.write('Total Loops:   ' + str(loop_count) +
                         '\nArena Battles: ' + str(self.arena_battles) +
                         '\nWorld Wins:    ' + str(self.world_successes) +
                         '\nWorld Losses:  ' + str(self.world_losses) +
                         '\nItems Gained:  ' + str(self.item_successes))





    # ARENA
    def arena_actions(self):
        # all the things we want to do in the arena screen
        try:
            self.goto('arena')
            self.challenge()
        except OutOfEnergy:
            self.log('RAN OUT OF ARENA ENERGY')
            self.goto('home')



    def challenge(self):
        # rematches every team possible
        challengers = self.bot.find_elements_by_class_name('-icon-challenge-return')
        rematch = []
        for ch in challengers:
            team = ch.get_attribute('data-teamid')
            if team in rematch or team in self.team_blacklist:
                continue
            sleep(rng(1, 5)) # 1 to 5 seconds
            ch.click()
            sleep(rng(3, 5))

            # check if we ran out of energy
            try:
                self.bot.find_element_by_class_name('c-overlay-message__text') # this element only appears if out of energy in which case a NoSuchElementException is raised
                raise OutOfEnergy
            except NoSuchElementException:
                pass

            self.arena_battles += 1
            self.log('challenged team #' + team)
            rematch.append(team)





    # WORLD
    def world_actions(self):
        # all the things we want to do in the world screen
        try:
            self.do_mission()
        except OutOfEnergy:
            self.log('RAN OUT OF WORLD ENERGY')



    def do_mission(self):
        # executes world mission
        # MUST BE MANUALLY EDITED BY HAND

        area_url = 'https://www.ninjamanager.com/world/area/anbu-hideout'
        mission_id = '199'
        data_url = '/world/area/anbu-hideout/mission/6'

        self.bot.get(area_url)
        sleep(rng(3, 6))
        mission = self.bot.find_element_by_xpath('//div[@data-missionid="' + mission_id + '"]')
        sleep(rng(1, 3))
        mission.find_element_by_xpath('./div[@class="c-mission-box__details"]/div[@class="c-mission-box__requirements"]/div[@class="c-mission-box__cost"]/div[@data-url="' + data_url + '"]').click() # fight button
        sleep(rng(4, 10))
        self.bot.find_element_by_class_name('pm-battle-buttons__skip').click() # skip button
        sleep(rng(5, 7))

        # check if we won or lost the mission
        if self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Victory':
            self.world_successes += 1
            self.log('world won')
        elif self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Defeat':
            self.world_losses += 1
            self.log('world lost')

        # check if we got the item
        try:
            self.bot.find_element_by_class_name('-status-done')
            self.log('ITEM GET')
            self.item_successes += 1
        except NoSuchElementException:
            self.log('no item')

        self.bot.find_element_by_class_name('pm-battle-buttons__finish').click() # finish button





    # GENERAL
    def check_energy(self):
        # checks how much energy we have
        self.goto('myteam')

        arena_bar = self.bot.find_element_by_class_name('header-team__bar-ae')
        arena_nrg = arena_bar.find_element_by_xpath('./div[@class="c-bar__text"]/span').text

        world_bar = self.bot.find_element_by_class_name('header-team__bar-we')
        world_nrg = world_bar.find_element_by_xpath('./div[@class="c-bar__text"]/span').text

        self.arena_energy = True
        if int(arena_nrg) < 4:
            self.arena_energy = False

        self.world_energy = True
        if int(world_nrg) < 7:
            self.world_energy = False

        self.log('Arena Energy = ' + arena_nrg)
        self.log('World Energy = ' + world_nrg)

        sleep(rng(20, 30))



    def goto(self, area: str):
        # navigates to a part of the website
        class_name = "-tab-" + area
        arena_button = self.bot.find_element_by_class_name(class_name)
        sleep(rng(0.5, 2))
        arena_button.click()
        sleep(rng(2, 8))



    def log(self, msg: str):
        # prints to console and file
        print(msg)
        self.logger.write('\n' + msg)





def rng(start: float, stop:float) -> float:
    # returns a random float between start and stop
    return uniform(start, stop)




if __name__ == "__main__":
    with open('headers.json', 'r') as file:
        headers = json.load(file)

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    NMBot = NMBot(headers, cookies)
    NMBot.execute()