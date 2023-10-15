# What is CafeteriaBot?
Basically, CafeteriaBot is a Telegram Bot that allows to look up what is on the menu in the Lahti campus of LUT cafeteria.
It allows user to look the menu on every day of the current week.

As per writing this (12.10.2023), the bot is **online** [here](https://t.me/lahti_cafeteria_bot)

However, Amazon AWS gives me only so much time to host it for free, so eventually it will go offilne if I don't get external funding.

The bot is separated in 2 parts:

* The bot
* Menu fetch 

### Menu fetch

The menu fetch uses menuapi from the ISKU website to pull information from API used

[Link to the menu website](https://www.compass-group.fi/ravintolat-ja-ruokalistat/foodco/kaupungit/lahti/isku-center/)

And scrapes the menu as a Python list wihich then stored locally as a .json


### Bot

Bot interacts with Telegram API through Python Telegram library and fetches a list from the .json

### ~~Scheduler~~

Scheduling is done with ```cron``` on Linux or Task Scheduler on Windows

## How to set it up on my machine?

These assume that you have Python 3.10.7 or higher and pip installed.

1. Clone the repository OR download a .ZIP
2. Unpack with 7-Zip in some folder, ex. CafeteriaBot, skip if you cloned the repo
3. Open your equivalent to Command Line in the directory:

For Windows users: Click RMB in the directory of the repo and click "Open in Terminal"
and enter this:
```
pip install -r requirements.txt
```
4. Go to your Telegram and find [@BotFather](https://t.me/BotFather) 
5. Enter ```/newbot``` and follow instructions
6. After you create a bot, you should recieve a HTTP API token, copy it: 
![Example](https://github.com/Login1990/CafeteriaBot/assets/79404334/fde9e0cb-f030-4369-bb22-97f7b3e1a71e)
7. Create a .env file in the same directory as you unpacked/cloned
8. Open this file as text and add following:
```
API_KEY="[YOUR API KEY]"
```
9. Run ```the_bot.py```
10. Script ```menu_fetch.py``` will fetch a .json with data, the menus are posted on Saturday for next week.
11. You will need to schedule this task weekly for automatic menu refreshment

Yay! You are done!

## Future plans

As you may know, besides the ISKU cafeteria there is also Niemi campus with actually decent food. I don't have any knowledge if they post it anywhere - but if they do, I will try to implement it ASAP.

## Contacts

Feel free to open issues or contact me directly at shamin2002@mail.ru
