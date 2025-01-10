import time
import os
from dotenv import load_dotenv
import random
import argparse
from natsort import natsorted
from publish_image import publish_image


def publish_all_images(directory, images, images_publication_frequency, telegram_channel_id, telegram_bot_token):
    for image in images:
        publish_image(directory, image, telegram_channel_id, telegram_bot_token)
        time.sleep(images_publication_frequency)    


def cycle_publish_images(directory, images_publication_frequency, telegram_channel_id, telegram_bot_token):
    images = natsorted(os.listdir(directory))
    publish_all_images(directory, images, images_publication_frequency, telegram_channel_id, telegram_bot_token)
    while True:
        random.shuffle(images)
        publish_all_images(directory, images, images_publication_frequency, telegram_channel_id, telegram_bot_token)    


if __name__ == "__main__":
    load_dotenv()
    images_publication_frequency = int(os.environ['IMAGES_PUBLICATION_FREQUENCY'])
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    parser = argparse.ArgumentParser(
        description='Публикация всех фотографий'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Путь к директории с изображениями',
    )
    args = parser.parse_args()
    cycle_publish_images(args.directory, images_publication_frequency, telegram_channel_id, telegram_bot_token)
