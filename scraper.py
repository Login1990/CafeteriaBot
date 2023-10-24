from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from deep_translator import GoogleTranslator
import requests as req 
import time
import json
import re

def scraper():
    # Here we are opening an ISKU website with no graphics, just pure data, but we have to load it since intersting data is provided by JavaScript
    web = req.get("https://www.pottusalvia.com/index.php/viikon-ruokalista/")

    soup = BeautifulSoup(web.text, "html.parser")

    element = soup.find("div", {"data-id": "eb498b1"})

    index = element.text.find("STUDENT`S MENU")
    result = element.text[index:]

    pattern = r'(\d+(?:,\d+)*)'

    result = re.sub(pattern, r'\1\n', result)

    days_pattern = r'Monday|Tuesday|Wednesday|Thursday|Friday'

    text_with_newlines = re.sub(days_pattern, '\n', result)

    text_list = text_with_newlines.split('\n')

    text_list = [item.strip() for item in text_list if item.strip()]

    text_list = text_list[4:]

    with open('relevant_data_niemi.json', 'w') as file:
        json.dump(text_list, file)

    return text_list
if __name__ == "__main__":
    scraper()