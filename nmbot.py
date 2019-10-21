from selenium.common.exceptions import *
from selenium import webdriver
from random import uniform
from time import sleep
import traceback
import json

from exceptions import *
import logger



class NMBot():
    def __init__(self, account, cookie, stats, logger, browser: str):
        self.stats = stats
        self.logger = logger

        self.load_mission(browser)
        self.logger.log('starting bot ...')

        if browser == 'chrome':
            self.bot = webdriver.Chrome(executable_path=r'drivers\chromedriver.exe')
        elif browser == 'firefox':
            self.bot = webdriver.Firefox(executable_path=r'drivers\geckodriver.exe')

        self.logger.log('navigating to ninjamanager.com ...')
        self.bot.get('https://www.ninjamanager.com')

        self.login(account)
        self.bot.add_cookie(cookie)
        self.logger.log('all checks successful')

        self.arena_energy = True
        self.world_energy = True

        self.team_blacklist = {'953','965'} # my teams



    def execute(self):
        try:
            self.logger.log('starting main loop ...')

            while True:
                self.logger.log('\n\n\n\n\n\n')
                self.check_energy()

                if self.arena_energy or self.world_energy:
                    self.logger.log('LOOP #' + str(self.stats['loop_count']) + '\n')

                    if self.arena_energy:
                        self.logger.log('starting arena challenges ...')
                        self.arena_actions()
                        self.logger.log('finished arena challenges\n')
                        self.slp(900, 1080) # 15 to 18 minutes
                    else:
                        self.logger.log('ARENA out of energy\n')

                    if self.world_energy:
                        self.logger.log('starting world missions ...')
                        self.world_actions()
                        self.logger.log('finished world missions')
                    else:
                        self.logger.log('WORLD out of energy')

                    self.stats['loop_count'] += 1

                self.slp(900, 1080) # 15 to 18 minutes
        except Exception as e:
            self.logger.log('\n\n\n\n\n\n')
            self.logger.log('%s' % e)
            self.logger.log(traceback.format_exc())





    # ARENA
    def arena_actions(self):
        # all the things we want to do in the arena screen
        try:
            self.goto('arena')
            self.challenge()
        except OutOfEnergy:
            self.logger.log('RAN OUT OF ARENA ENERGY')
            self.bot.get('https://www.ninjamanager.com')



    def challenge(self):
        # rematches every team possible
        challengers = self.bot.find_elements_by_class_name('-icon-challenge-return')
        rematch = []

        if not challengers:
            self.logger.log('no challenges')
            return

        for ch in challengers:
            try:
                team = ch.get_attribute('data-teamid')
                if team in rematch or team in self.team_blacklist:
                    continue
                self.slp(1, 5) # 1 to 5 seconds
                ch.click()
                self.slp(3, 5)

                # perform some checks
                try:
                    overlay = self.bot.find_element_by_class_name('c-overlay-message__text') # this element only appears if out of energy or max challenges
                    if 'too many opponents' in overlay.text:
                        rematch.append(team)
                        raise MaxChallenges
                    elif 'energy' in overlay.text:
                        raise OutOfEnergy
                except NoSuchElementException:
                    pass

                self.stats['arena_battles'] += 1
                self.logger.log('challenged team #' + team)
                rematch.append(team)
            except MaxChallenges:
                self.logger.log('could not challenge team #' + team + '. reached max challenges')
            except (ElementClickInterceptedException, ElementNotInteractableException):
                self.logger.log('could not challenge team #' + team + '. unable to click element.')





    # WORLD
    def world_actions(self):
        # all the things we want to do in the world screen
        try:
            self.do_mission()
        except OutOfEnergy:
            self.logger.log('RAN OUT OF WORLD ENERGY')



    def do_mission(self):
        # executes world mission
        # MUST BE MANUALLY EDITED BY HAND

        self.bot.get(self.area_url)
        self.slp(3, 6)
        self.bot.find_element_by_xpath('//div[@data-url="' + self.area_url[self.area_url.find('/world'):] + '/mission/' + self.mission_num + '"]').click() # fight button
        self.slp(4, 10)
        self.bot.find_element_by_class_name('pm-battle-buttons__skip').click() # skip button
        self.slp(5, 7)

        # check if we won or lost the mission
        if self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Victory':
            self.stats['world_successes'] += 1
            self.logger.log('world won')
        elif self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Defeat':
            self.stats['world_losses'] += 1
            self.logger.log('world lost')

        # check if we got the item
        try:
            self.bot.find_element_by_class_name('-status-done')
            self.logger.log('ITEM GET')
            self.stats['item_successes'] += 1
        except NoSuchElementException:
            self.logger.log('no item')

        self.bot.find_element_by_class_name('pm-battle-buttons__finish').click() # finish button





    # GENERAL
    def login(self, account):
        self.logger.log('logging in ...')
        self.bot.find_element_by_class_name('header-inside__account-login').click()
        self.slp(3, 6)
        self.bot.find_element_by_id('input-login').send_keys(account['username'])
        self.slp(2, 5)
        self.bot.find_element_by_id('input-password').send_keys(account['password'])
        self.slp(2, 5)
        self.bot.find_element_by_id('login-nm-button').click()
        self.slp(10, 15)

        assert "Home" in self.bot.title, 'LOGIN FAILED'
        self.logger.log('login successful')



    def load_mission(self, browser: str):
        # updates mission data from json file
        with open('json_txt/world.json', 'r') as file:
            data = json.load(file)

        self.area_url = data[browser]['area_url']
        self.mission_num = data[browser]['mission_num']



    def slp(self, min: float, max: float):
        # sleeps for a random amount of time between min and max
        sleep(uniform(min, max))



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

        self.logger.log('Arena Energy = ' + arena_nrg)
        self.logger.log('World Energy = ' + world_nrg)

        self.slp(20, 30)



    def goto(self, area: str):
        # navigates to a part of the website
        class_name = "-tab-" + area
        area_button = self.bot.find_element_by_class_name(class_name)
        self.slp(0.5, 2)
        area_button.click()
        self.slp(4, 8)



    def stop(self):
        # closes the browser
        self.logger.log('\n\n\nclosing bot')
        self.bot.quit()