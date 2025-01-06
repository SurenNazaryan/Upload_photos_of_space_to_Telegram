import requests
import os
import argparse
from working_with_files import file_writing
from http_utils import fetch_response, fetch_response_data


def fetch_spacex_launch_images(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response_data = fetch_response_data(url, params=None)
    links = response_data['links']['flickr']['original']
    directory = 'spacex_launch_images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for index, link in enumerate(links, start=1):
        response = fetch_response(link, params=None)
        filename = f'spacex_{index}.jpg'
        file_writing(directory, filename, response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Получение фото запуска и их скачивание'
    )
    parser.add_argument(
        '--launch_id',
        type=str,
        help='ID запуска',
        default='latest'
    )
    args = parser.parse_args()
    launch_id = args.launch_id
    fetch_spacex_launch_images(args.launch_id)
