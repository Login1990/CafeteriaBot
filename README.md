# What is CafeteriaBot?
Basically, CafeteriaBot is a Telegram Bot that allows to look up what is on the menu in the Lahti campus of LUT cafeteria.
It allows user to look the menu on every day of the current week.

As per writing this (12.10.2023), the bot is **online** [here](https://t.me/lahti_cafeteria_bot)
However, Amazon AWS gives me only so much time to host it for free, so eventually it will go offilne if I don't get external funding.

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

These assume that you have Python 3.10.7 or higher and pip installed.

1. Clone the repository OR download a .ZIP
2. Unpack with 7-Zip in some folder, ex. CafeteriaBot, skip if you cloned the repo
3. 
4. Go to your Telegram and find [@BotFather](https://t.me/BotFather) 
5. Enter ```/newbot``` and follow instructions
6. After you create a bot, you should recieve a HTTP API token, copy it: 
![Example](https://github.com/Login1990/CafeteriaBot/assets/79404334/fde9e0cb-f030-4369-bb22-97f7b3e1a71e)
7. Create a .env file in the same directory as you unpacked/cloned
8. Open this file and add following:
```
API_KEY="[YOUR API KEY]"
```
9. After that, you simply need to launch 2 scripts at the same time: ```scheduler.py``` and ```the_bot.py```, it will require 2 terminals as both of these scripts are blocking code
~~OR wait until I will fix it, works fine rn~~

Yay! You are done!

## Future plans

As you may know, besides the ISKU cafeteria there is also Niemi campus with actually decent food. I don't have any knowledge if they post it anywhere - but if they do, I will try to implement it ASAP.

The code is being run in 2 terminals which is unoptimal. ~~but fine~~ so I will try to address it later.
