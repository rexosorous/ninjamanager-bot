import json



def get_account(browser: str) -> dict:
    with open('json_txt/accounts.json', 'r') as file:
        accounts = json.load(file)
    return accounts[browser]



def get_cookie(browser: str) -> dict:
    with open('json_txt/cookies.json', 'r') as file:
        cookies = json.load(file)
    return cookies[browser]



def get_options() -> dict:
    # loads all options
    with open('json_txt/config.json', 'r') as file:
        data = json.load(file)
    return data



def save_options(data: dict):
    # saves options
    with open('json_txt/config.json', 'w') as file:
        json.dump(data, file)



def fix_location(item_data: dict) -> str:
    # makes the locations easier to read
    location = item_data['location']
    if 'Shop' in location:
        return location
    location = location[location.find('area')+5:].replace('-', ' ')
    return location + ' #' + item_data['mission']