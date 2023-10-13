
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
import time
import json

def scraper():
    # Here we are opening an ISKU website with no graphics, just pure data, but we have to load it since intersting data is provided by JavaScript
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.compass-group.fi/ravintolat-ja-ruokalistat/foodco/kaupungit/lahti/isku-center/")

    # This section manipulates the page a bit, ensuring that it is properly and fully loaded before we do any operations
    for _ in range(5):  # Adjust the number of times you want to scroll as needed
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Adjust the sleep time as needed
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'lunch-menu-block__manual-menu')))

    # Not only needed data is in JS, not HTML, it is also hidden behind a button, it is needed to find the button and then locate interesting
    # And once again wait until it loads
    text_to_find = "Koko viikko"
    button = driver.find_element(By.XPATH, f"//*[text()='{text_to_find}']")
    button.click()
    page_source = driver.page_source
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    revealed_text_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'lunch-menu-block__week-change')))

    time.sleep(3)

    soup = BeautifulSoup(page_source, 'html.parser')

    # Instead of crawling through the HTML we simply request a class that holds the text through JavaScript injection
    js_script = "return Array.from(document.getElementsByClassName('lunch-menu-block__manual-menu compass-rich-text'));"
    revealed_text = driver.execute_script(js_script)
    list_of_elements = []
    for x in revealed_text:
        list_of_elements.append(x.text)
    driver.quit()
    with open('relevant_data.json', 'w') as file:
        json.dump(list_of_elements, file)
    return list_of_elements



if __name__ == "__main__":
    scraper()