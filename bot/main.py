import logging as logger
import os
import asyncio
from dotenv import load_dotenv

from telebot.async_telebot import AsyncTeleBot


load_dotenv()

print(os.getenv('BOT_TOKEN'))

bot = AsyncTeleBot(token="6267833990:AAEusxDRjrQkzriti69TrSKDsaRSDPlarpI")

@bot.message_handler(commands=['help','start'])
async def send_welcome(message):
    logger.log(level=1, msg=message)
    await bot.reply_to(message, """ Sanya hui sosi """)


@bot.message_handler(func=lambda message: message=True )
async def rec_message(message):
     logger.log(level=1, msg=message)    
     await bot.reply_to(message, """ Sanya hui sosi """)
asyncio.run(bot.polling())