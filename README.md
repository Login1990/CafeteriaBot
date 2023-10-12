# What is CafeteriaBot?
Basically, CafeteriaBot is a Telegram Bot that allows to look up what is on the menu in the Lahti campus of LUT cafeteria.
It allows user to look the menu on every day of the current week.

The bot is separated in 3 parts:

* The scraper
* The bot
* ~~And the ugly~~
* And the scheduler

### Scraper

The scraper interacts with JavaScript on the ISKU website where menu is posted each week 

[Link to the menu website](https://www.compass-group.fi/ravintolat-ja-ruokalistat/foodco/kaupungit/lahti/isku-center/)

And scrapes the menu as a Python list wihich then stored locally as a .json

NB! As per writing this (12.10.2023), the scraper works - however I have written in 2 times all over because ISKU keeps changing their website.

### Bot

Bot interacts with Telegram API through Python Telegram library and fetches a list from the .json

### Scheduler

Is a simple module that refreshes fetched .json every day at 2:00

## How to set it up on my machine?

1. Clone the repository OR download a .ZIP
2. Unpack with 7-Zip in some folder, ex. CafeteriaBot, skip if you cloned the repo
3. Go to your Telegram and find [@BotFather](https://t.me/BotFather) 
4. Enter ```/newbot``` and follow instructions
5. 
![изображение](https://github.com/Login1990/CafeteriaBot/assets/79404334/fde9e0cb-f030-4369-bb22-97f7b3e1a71e)

6. Create a .env file in the same directory as you unpacked/cloned


This is a repository for a bot that helps me to figure out what is for lunch at my university
