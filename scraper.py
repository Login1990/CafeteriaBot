
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
#import translators as ts
from deep_translator import GoogleTranslator
import time
import json
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://www.foodandco.fi/ravintolat/Ravintolat-kaupungeittain/lahti/iskucenter/")
#content = driver.page_source
#soup = BeautifulSoup(content)
#for a in soup.findAll('a',href=True, attrs={'class':'menu-container-menu-content-custom ng-binding ng-scope'}):
#    name=a.find('strong')
#    print(name)

#response = requests.get("https://www.foodandco.fi/ravintolat/Ravintolat-kaupungeittain/lahti/iskucenter/printdaymenu/")
#soup = BeautifulSoup(response.content, 'html.parser')
#x = soup.find(class_="restaurant-menu-items")
#y = x.find("p")
#print(x)
#print()
#print(y)#

def scraper():
    days = []
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.compass-group.fi/ravintolat-ja-ruokalistat/foodco/kaupungit/lahti/isku-center/")
    #x = driver.find_element(By.ID, "menuContainer")
    #y = driver.find_elements(By.CLASS_NAME,"lunch-menu-block__manual-menu compass-rich-text")
    print()
    for _ in range(5):  # Adjust the number of times you want to scroll as needed
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Adjust the sleep time as needed
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'lunch-menu-block__manual-menu')))
    text_to_find = "Koko viikko"
    button = driver.find_element(By.XPATH, f"//*[text()='{text_to_find}']")
    button.click()
    #print(button.text)
    page_source = driver.page_source
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    revealed_text_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'lunch-menu-block__week-change')))
    #print(page_source)
    time.sleep(3)
    soup = BeautifulSoup(page_source, 'html.parser')
    menu_elements = soup.find_all(class_='lunch-day')
    #print(menu_elements)
    js_script = "return Array.from(document.getElementsByClassName('lunch-menu-block__manual-menu compass-rich-text'));"  # Replace with the actual ID of the updated element
    revealed_text = driver.execute_script(js_script)
    #print(revealed_text)
    list_of_elements = []
    for x in revealed_text:
        list_of_elements.append(x.text)
    #for menu_element in menu_elements:
    #    menu_text = menu_element.get_text()
    #    print(menu_text)
    #for h in y:
    #    print(h)
    #    x = h.get_attribute("innerHTML")
    ##    cleantext = BeautifulSoup(x, 'lxml').text
    #    days.append(cleantext)
    #    #print(cleantext)
    #    #print()
    #for x in range(len(days)):
    #    days[x] = days[x].replace(")","\n")
    #    days[x] = days[x].replace("(","")
    #    #print(days[x])
    driver.quit()
    with open('relevant_data.json', 'w') as file:
        json.dump(list_of_elements, file)
    return list_of_elements
    #b = y.find_elements(By.TAG_NAME,"p")
    #for h in b:
        #o = h.get_attribute("innerHTML")
        #cleantext = BeautifulSoup(o, 'lxml').text
        #for x in range(len(cleantext)):
        #    if cleantext[x] == ")":
        #        print("I am here")
        #        cleantext[x+1] = '\n'
        #cleantext.replace(')',')\n')
        #print(cleantext)

    #for h in b:
    #    h.find_elements(By.TAG_NAME,"br")
    #    print(h.get_attribute("innerHTML"))

    #print(b.get_attribute("innerHTML")) 
    #z = y.get_attribute("innerHTML")
    #print(z)
    
#x = scraper()
#y = x[0].split("\n")

#for x in y:
    #print(GoogleTranslator(source='fi', target='en').translate(x))
#print(GoogleTranslator(source='fi', target='en').translate(x[0]))
if __name__ == "__main__":
    scraper()