import requests
import os
import json
import random


with open('headers.json', 'r') as file:
    HEADERS = json.load(file)

with open('cookies.json', 'r') as file:
    COOKIES = json.load(file)


class NMBot():
    def __init__():
        self.session = requests.Session()


    def main_loop():
        while True:
            try:
                challengers = self.get_challengers()
                random.uniform()
            except FileNotFoundError:
                print('error opening response.txt')


    def get_challengers() -> set(str):
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
        self.session.post('https://www.ninjamanager.com/ajax/challengeTeam', headers=HEADERS, cookies=COOKIES, data={'TeamID': team_id,'SkipBattle': 'true'})