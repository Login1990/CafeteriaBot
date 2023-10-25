import logging             #Don't know what it does, documentation uses it
from telegram import *
from telegram.ext import (            #Telegram API
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
    ContextTypes
)
from deep_translator import GoogleTranslator #Website is in Finnish, translation is required
from datetime import date
import time
import json
from dotenv import load_dotenv
import os



logging.basicConfig( #No idea, leave it be
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


options_lahti = ["Mukkulankatu Cafeteria","Today: Mukkulankatu","Monday: Mukkulankatu","Tuesday: Mukkulankatu","Wendsday: Mukkulankatu","Thursday: Mukkulankatu","Friday: Mukkulankatu"]
options_niemi = ["Niemi Cafeteria","Today: Niemi","Monday: Niemi","Tuesday: Niemi","Wendsday: Niemi","Thursday: Niemi","Friday: Niemi"]
#print(help(ts.deepl))

    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): #When you start with bot 
    buttons = [[KeyboardButton(options_lahti[0]), KeyboardButton(options_niemi[0]),KeyboardButton("Tell me about me")]]
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!\nThis bot is displaying a menu for this week in LUT Lahti Campus and ", reply_markup=ReplyKeyboardMarkup(buttons))

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE): #Main message handler, on each stage you have button tiles to proceed or back down
    user = update.message.from_user
    print("User",user['username'],"has used the bot!")
    with open("relevant_data.json","r") as file:
        information_mukkulankatu = json.load(file)
    with open("relevant_data_niemi.json","r") as file:
        information_niemi = json.load(file)
    if "Tell me about me" in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Here is all what I can get on you:\nYour username: {user['username']}\nYour user id: {user['id']}\nYour name: {user['first_name']}\nYour surname: {user['last_name']}")
    if "<- Back" in update.message.text:
        buttons = [[KeyboardButton(options_lahti[0]), KeyboardButton(options_niemi[0]),KeyboardButton("Tell me about me")]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!\nThis bot is displaying a menu for this week in LUT Lahti Campus", reply_markup=ReplyKeyboardMarkup(buttons))
    elif options_lahti[0] in update.message.text:
        #print("he")
        buttons = [[KeyboardButton("<- Back")],[KeyboardButton(options_lahti[1])],[KeyboardButton(options_lahti[2])],[KeyboardButton(options_lahti[3])],[KeyboardButton(options_lahti[4])],[KeyboardButton(options_lahti[5])],[KeyboardButton(options_lahti[6])]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="What day?", reply_markup=ReplyKeyboardMarkup(buttons))
    elif options_lahti[1] in update.message.text:
        try:
            today = date.today()
            await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
            if len(information_mukkulankatu) < today.weekday():
                raise IndexError
            x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[today.weekday()])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[today.weekday()])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
        except IndexError:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Today there is no menu.")
    elif options_lahti[2] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[(len(information_mukkulankatu)-5)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[(len(information_mukkulankatu)-5)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options_lahti[3] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[(len(information_mukkulankatu)-4)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[(len(information_mukkulankatu)-4)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options_lahti[4] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[(len(information_mukkulankatu)-3)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[(len(information_mukkulankatu)-3)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options_lahti[5] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[(len(information_mukkulankatu)-2)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[(len(information_mukkulankatu)-2)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options_lahti[6] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information_mukkulankatu[(len(information_mukkulankatu)-1)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_mukkulankatu[(len(information_mukkulankatu)-1)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options_niemi[0] in update.message.text:
        buttons = [[KeyboardButton("<- Back")],[KeyboardButton(options_niemi[1])],[KeyboardButton(options_niemi[2])],[KeyboardButton(options_niemi[3])],[KeyboardButton(options_niemi[4])],[KeyboardButton(options_niemi[5])],[KeyboardButton(options_niemi[6])]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="What day?", reply_markup=ReplyKeyboardMarkup(buttons))
    elif options_niemi[1] in update.message.text:
        try:
            today = date.today()
            if len(information_niemi) < today.weekday():
                raise IndexError
            x = GoogleTranslator(source='fi', target='en').translate(information_niemi[today.weekday()])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[today.weekday()])
        except IndexError:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Today there is no menu.")
    elif options_niemi[2] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[0])
    elif options_niemi[3] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[1])
    elif options_niemi[4] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[2])
    elif options_niemi[5] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[3])
    elif options_niemi[5] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information_niemi[4])
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Unknown command, try using /start")
if __name__ == '__main__':
    load_dotenv()
    api_token = os.getenv("API_KEY") #Purely theorethically, you can enter your API_KEY right here, but it is a bad practice to add credentials to code directly
    application = ApplicationBuilder().token(api_token).build() #Building the app, token is private
    start_handler = CommandHandler('start', start) #This command stands that now if you type /start in chat, you activate start() function
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler) #Everything that is not a command, is thrown against the message_handler function
    application.add_handler(start_handler)  #Activate handlers
    application.add_handler(message_handler)
    application.run_polling() #Activate app
            