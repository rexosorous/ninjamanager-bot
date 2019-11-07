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

        self.check_gold()
        self.stats['gold_gained'] = 0

        self.arena_energy = True
        self.world_energy = True

        self.team_blacklist = {'953','965'} # my teams



    def execute(self):
        self.logger.log('starting main loop ...')

        while True:
            try:
                self.logger.log('\n\n\n\n\n\n')
                self.check_energy()

                if self.arena_energy or self.world_energy:
                    self.logger.log('LOOP #' + str(self.stats['loop_count']) + '\n')

                    if self.arena_energy:
                        self.logger.log('starting arena challenges ...')
                        challenge_count = self.arena_actions()
                        self.logger.log('finished arena challenges\n')
                        if challenge_count > 0:
                            self.check_gold()
                            self.slp(780, 960) # 13 to 16 minutes
                        else:
                            self.slp(60, 180) # 1 to 3 minutes
                    else:
                        self.logger.log('ARENA out of energy\n')

                    if self.world_energy:
                        self.logger.log('starting world missions ...')
                        self.world_actions()
                        self.logger.log('finished world missions')
                        self.check_gold()
                    else:
                        self.logger.log('WORLD out of energy')

                    self.stats['loop_count'] += 1

                self.slp(780, 960) # 13 to 16 mintues
            except ConnectionRefusedError:
                return
            except Exception as e:
                self.logger.log('\n\n\n\n\n\n')
                self.logger.log('error during main loop. will try to restart after 15 minutes')
                self.logger.log('error:')
                self.logger.log('%s' % e)
                self.logger.log(traceback.format_exc())
                self.goto('home')
                sleep(900) # 15 minutes





    # ARENA
    def arena_actions(self):
        # all the things we want to do in the arena screen
        try:
            self.goto('arena')
            return self.challenge()
        except OutOfEnergy:
            self.logger.log('RAN OUT OF ARENA ENERGY')
            self.bot.get('https://www.ninjamanager.com')



    def challenge(self) -> int:
        # rematches every team possible
        challengers = self.bot.find_elements_by_class_name('-icon-challenge-return')
        rematch = []
        challenge_count = 0

        if not challengers:
            self.logger.log('no challenges')
            return 0

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
                    if 'too many opponents' in overlay.text or 'max amount of challenges' in overlay.text:
                        rematch.append(team)
                        self.bot.find_element_by_class_name('c-overlay-message__close').click()
                        raise MaxChallenges
                    elif 'energy' in overlay.text:
                        raise OutOfEnergy
                    else:
                        raise UnknownException
                except NoSuchElementException: # operating as normal
                    self.stats['arena_battles'] += 1
                    challenge_count += 1
                    self.logger.log('   challenged team #' + team)
                    rematch.append(team)
            except MaxChallenges:
                self.logger.log('   could not challenge team #' + team + '. reached max challenges')
            except (ElementClickInterceptedException, ElementNotInteractableException):
                self.logger.log('   could not challenge team #' + team + '. unable to click element.')
            except UnknownException:
                self.logger.log('   could not challenge team #' + team + '. unknown reason')
                try:
                    self.bot.find_element_by_class_name('c-overlay-message__close').click()
                except NoSuchElementException:
                    pass

        return challenge_count





    # WORLD
    def world_actions(self):
        # all the things we want to do in the world screen
        try:
            self.bot.get(self.area_url)
            self.do_mission()
        except OutOfEnergy:
            self.logger.log('RAN OUT OF WORLD ENERGY')



    def do_mission(self):
        # executes world mission
        try:
            self.slp(10, 20)
            self.bot.find_element_by_xpath('//div[@data-url="' + self.area_url[self.area_url.find('/world'):] + '/mission/' + self.mission_num + '"]').click() # fight button
            self.slp(10, 20)
            self.bot.find_element_by_class_name('pm-battle-buttons__skip').click() # skip button
            self.slp(10, 20)

            # check if we won or lost the mission
            if self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Victory':
                self.stats['world_successes'] += 1
                self.logger.log('world won')
            elif self.bot.find_element_by_class_name('pm-battle-matchup__title').text == 'Defeat':
                self.stats['world_losses'] += 1
                self.logger.log('world lost')

            # check if we got any items
            try:
                items = self.bot.find_elements_by_class_name('pm-battle-treasures__drop')
                for i in items:
                    item_name = i.find_element_by_xpath('./div[@class="c-item -size-l h-item-material-1    js-item-tooltip"]/div[@class="c-item__name  a-item-name"]').text
                    if '-status-failed' in i.get_attribute('class'):
                        self.logger.log('   failed to get item ' + item_name)
                    elif '-status-done' in i.get_attribute('class'):
                        self.logger.log('   obtained item ' + item_name)
                        if item_name in self.stats['items_gained'].keys():
                            self.stats['items_gained'][item_name] += 1
                        else:
                            self.stats['items_gained'][item_name] = 1
            except NoSuchElementException:
                self.logger.log('   mission has no item drops')

            self.bot.find_element_by_class_name('pm-battle-buttons__finish').click() # finish button
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.logger.log('   error - could not click on world mission buttons')






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

        if "Home" not in self.bot.title:
            raise LoginFailure

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



    def check_gold(self):
        # checks how much gold we have and how much gold we've earned
        gold_bar = self.bot.find_element_by_class_name('header-team__resource-gold')
        gold_amt = gold_bar.find_element_by_xpath('./span').text
        gold_amt = gold_amt.replace(',', '')

        old_gold = self.stats['gold']
        self.stats['gold'] = int(gold_amt)
        self.stats['gold_gained'] += (self.stats['gold'] - old_gold)



    def goto(self, area: str):
        # navigates to a part of the website
        class_name = "-tab-" + area
        area_button = self.bot.find_element_by_class_name(class_name)
        self.slp(0.5, 2)
        area_button.click()
        self.slp(4, 8)



    def stop(self):
        # closes the browser
        self.logger.log('\n\n\nclosing bot ...\n')
        self.bot.quit()