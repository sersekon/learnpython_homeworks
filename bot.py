
import logging

import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду /start')
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def talk_to_me(update, context):
     user_text = update.message.text 
     user_text = update.message.text
     print(user_text)
     update.message.reply_text(user_text)

def echo_planet(update, context):
    text = 'Вызвана команда /planet'
    print(text)
    user_input = update.message.text.split()[-1]
    planet = getattr(ephem, user_input)(datetime.date.today())
    const = ephem.constellation(planet)
    const = user_input + ' находится в созвездии {}'.format(const[1])
    update.message.reply_text(const)
    
    

def main():
    mybot = Updater("875472318:AAFxl-pcYtpwhoqz51zqdoQF5NuhD-CP3Xk", use_context=True, request_kwargs=PROXY) 
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", echo_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
     main()  

