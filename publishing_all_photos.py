from telegram import Bot
import time
import os
from dotenv import load_dotenv
import random
import argparse
from natsort import natsorted


def image_publication(directory, image_list):
    channel_id = os.environ["CHANNEL_ID"]
    publication_frequency = int(os.environ["PUBLICATION_FREQUENCY"])
    bot_token = os.environ["BOT_TOKEN"]
    bot = Bot(token=bot_token)
    for image in image_list:
        bot.send_photo(
            chat_id=channel_id,
            photo=open(f'{directory}/{image}', 'rb')
        )
        time.sleep(publication_frequency)


def main(directory):
    image_list = natsorted(os.listdir(directory))
    image_publication(directory, image_list)
    while True:
        random.shuffle(image_list)
        image_publication(directory, image_list)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Публикация всех фотографий'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Путь к директории с изображениями',
    )
    args = parser.parse_args()
    main(args.directory)
