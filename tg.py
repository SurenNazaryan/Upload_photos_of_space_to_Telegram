from telegram import Bot
import os
from dotenv import load_dotenv


load_dotenv()
bot_token = os.environ["BOT_TOKEN"]
channel_id = os.environ["CHANNEL_ID"]
bot = Bot(token=bot_token)
bot.send_photo(chat_id=channel_id, photo=open(f'example/example.jpeg', 'rb'))