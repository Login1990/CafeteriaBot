import requests
import json
import datetime
from bs4 import BeautifulSoup
from scraper import scraper

def fetch_menu_data():
    global latest_menu_data, last_menu_fetch
    date = datetime.datetime.now()
    date = date + datetime.timedelta(days=3)
    date = date.strftime('%Y-%m-%d')
    response_API = requests.get(f"https://www.compass-group.fi/menuapi/week-menus?costCenter=3424&date={date}&language=fi")
    y = json.loads(response_API.text)
    return y

def parse_json():
    list1 = [fetch_menu_data()["menus"][x]["html"] for x in range(5)]
    return list1

def clean_tags():
    dirty_list = parse_json()
    for x in range(len(dirty_list)):
        soup = BeautifulSoup(dirty_list[x], 'html.parser')
        dirty_list[x] = soup.get_text()
    with open('relevant_data.json', 'w') as file:
        json.dump(dirty_list, file)
    return dirty_list

def dump_json():
    clean_tags()

if __name__ == "__main__":
    dump_json()
    scraper()