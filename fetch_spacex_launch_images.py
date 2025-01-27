import requests
import os
import argparse
from working_with_files import writing_file


def fetch_spacex_launch_images(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    response= response.json()
    links = response['links']['flickr']['original']
    directory = 'spacex_launch_images'
    os.makedirs(directory, exist_ok=True)
    for index, link in enumerate(links, start=1):
        response = requests.get(link)
        response.raise_for_status()
        file_name = f'spacex_{index}.jpg'
        writing_file(directory, file_name, response)


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
    fetch_spacex_launch_images(args.launch_id)
