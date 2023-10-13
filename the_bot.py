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


options = ["Cafeteria Menu","Today","Monday","Tuesday","Wendsday","Thursday","Friday"]
#print(help(ts.deepl))

    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): #When you start with bot 
    buttons = [[KeyboardButton(options[0]),KeyboardButton("Tell me about me")]]
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!\nThis bot is displaying a menu for this week in LUT Lahti Campus", reply_markup=ReplyKeyboardMarkup(buttons))

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE): #Not used, can echo your messages
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE): #Not used, can make your text BIG
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE): #Main message handler, on each stage you have button tiles to proceed or back down
    user = update.message.from_user
    print("User",user['username'],"has used the bot!")
    with open("relevant_data.json","r") as file:
        information = json.load(file)   
    if "Tell me about me" in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Here is all what I can get on you:\nYour username: {user['username']}\nYour user id: {user['id']}\nYour name: {user['first_name']}\nYour surname: {user['last_name']}")
    if "<- Back" in update.message.text:
        buttons = [[KeyboardButton(options[0]),KeyboardButton("Tell me about me")]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!\nThis bot is displaying a menu for this week in LUT Lahti Campus", reply_markup=ReplyKeyboardMarkup(buttons))
    elif options[0] in update.message.text:
        #print("he")
        buttons = [[KeyboardButton("<- Back")],[KeyboardButton(options[1])],[KeyboardButton(options[2])],[KeyboardButton(options[3])],[KeyboardButton(options[4])],[KeyboardButton(options[5])],[KeyboardButton(options[6])]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="What day?", reply_markup=ReplyKeyboardMarkup(buttons))
    elif options[2] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information[(len(information)-5)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information[(len(information)-5)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options[3] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information[(len(information)-4)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information[(len(information)-4)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options[4] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information[(len(information)-3)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information[(len(information)-3)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options[5] in update.message.text: 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information[(len(information)-2)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information[(len(information)-2)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options[6] in update.message.text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
        x = GoogleTranslator(source='fi', target='en').translate(information[(len(information)-1)])
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=information[(len(information)-1)])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    elif options[1] in update.message.text:
        try:
            today = date.today()
            await context.bot.send_message(chat_id=update.effective_chat.id, text="English was worked on, test it out, still wouldn't trust it with your life")
            if len(information) < today.weekday():
                raise IndexError
            x = GoogleTranslator(source='fi', target='en').translate(information[today.weekday()])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=information[today.weekday()])
            await context.bot.send_message(chat_id=update.effective_chat.id, text=x)
        except IndexError:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Today there is no menu.")
if __name__ == '__main__':
    load_dotenv()
    api_token = os.getenv("API_KEY") #Purely theorethically, you can enter your API_KEY right here, but it is a bad practice to add credentials to code directly
    application = ApplicationBuilder().token(api_token).build() #Building the app, token is private
    start_handler = CommandHandler('start', start) #This command stands that now if you type /start in chat, you activate start() function
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler) #Everything that is not a command, is thrown against the message_handler function
    application.add_handler(start_handler)  #Activate handlers
    application.add_handler(message_handler)
    application.run_polling() #Activate app
            