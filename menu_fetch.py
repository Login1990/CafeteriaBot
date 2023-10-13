import requests
import json
import datetime
from bs4 import BeautifulSoup

def fetch_menu_data():
    global latest_menu_data, last_menu_fetch
    date = datetime.datetime.now()
    date = date.strftime('%Y-%m-%d')
    response_API = requests.get(f"https://www.compass-group.fi/menuapi/week-menus?costCenter=3424&date={date}&language=fi")
    y = json.loads(response_API.text)
    return y

def parse_json():
    list = []
    json_data = fetch_menu_data()
    for x in range(0, 5):
        list.append(json_data["menus"][x]["html"])
    return list

def clean_tags():
    dirty_list = parse_json()
    for x in range(len(dirty_list)):
        soup = BeautifulSoup(dirty_list[x], 'html.parser')
        dirty_list[x] = soup.get_text()
    with open('relevant_data.json', 'w') as file:
        json.dump(dirty_list, file)
    return dirty_list

if __name__ == "__main__":
    clean_tags()