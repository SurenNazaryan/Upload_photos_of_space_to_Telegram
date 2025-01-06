from telegram import Bot
import os
from dotenv import load_dotenv
import random
import argparse


def image_publication(directory, image):
    channel_id = os.environ["CHANNEL_ID"]
    publication_frequency = int(os.environ["PUBLICATION_FREQUENCY"])
    bot_token = os.environ["BOT_TOKEN"]
    bot = Bot(token=bot_token)
    image_list = os.listdir(directory)
    random_image = random.choice(image_list)   
    if image == '':
        bot.send_photo(
            chat_id=channel_id,
            photo=open(f'{directory}/{random_image}', 'rb')
        )
    else:
        bot.send_photo(
            chat_id=channel_id,
            photo=open(f'{directory}/{image}', 'rb')
        )


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Публикация одной фотографии'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Путь к директории с изображениями',
    )
    parser.add_argument(
        '--image',
        type=str,
        help='Имя изображения. Если не указано, будет выбрано случайное изображение.',
        default=''
    )
    args = parser.parse_args()
    image_publication(args.directory, args.image)