from telegram import Bot
import os


def publish_image(directory, image_to_send, telegram_channel_id, telegram_bot_token):
    bot = Bot(token=telegram_bot_token)
    with open(f'{directory}/{image_to_send}', 'rb') as photo_file: 
        bot.send_photo(
            chat_id=telegram_channel_id,
            photo=photo_file
        )
