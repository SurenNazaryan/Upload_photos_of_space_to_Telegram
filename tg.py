from telegram import Bot
import os
from dotenv import load_dotenv


load_dotenv()
bot_token = os.environ["BOT_TOKEN"]
channel_id = os.environ["CHANNEL_ID"]
bot = Bot(token=bot_token)
bot.send_message(chat_id=channel_id, text='Текст')