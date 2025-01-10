import os
from dotenv import load_dotenv
import random
import argparse
from publish_image import publish_image


def publish_random_or_selected_image(directory, telegram_channel_id, telegram_bot_token, image_to_send=None):
    if image_to_send is None:
        images = os.listdir(directory)
        image_to_send = random.choice(images)
    publish_image(directory, image_to_send, telegram_channel_id, telegram_bot_token)


if __name__ == '__main__':
    load_dotenv()
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    parser = argparse.ArgumentParser(
        description='Публикация случайной или указанной фотографии'
    )
    parser.add_argument(
        'directory',
        type=str,
        help='Путь к директории с изображениями',
    )
    parser.add_argument(
        '--image_to_send',
        type=str,
        help='Имя изображения. Если не указано, будет выбрано случайное изображение.',
        default=None
    )
    args = parser.parse_args()
    publish_random_or_selected_image(args.directory, telegram_channel_id, telegram_bot_token, args.image_to_send)

