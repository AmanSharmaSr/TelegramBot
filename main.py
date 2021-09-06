import os
import telebot



API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['getsocial'])
def getsocial(message):
  bot.send_message(message.chat.id, "@ASJrLp_bot 1")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['roastAshmit'])
def hola(message):
  bot.send_message(message.chat.id, "Chup bilkl chup spanish ke chode!")

@bot.message_handler(commands=['getaminemrating'])
def getaminemrating(message):
  bot.reply_to(message, "@gsamansharma , You have been summoned! Activate Aminem")

@bot.message_handler(commands=['getmemanrating'])
def getmemanrating(message):
  bot.reply_to(message, "@gsamansharma , You have been summoned! Activate Meman")
bot.polling()
