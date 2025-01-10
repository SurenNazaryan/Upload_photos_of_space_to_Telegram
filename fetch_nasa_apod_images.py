import requests
import os
from dotenv import load_dotenv
from working_with_files import writing_file, get_file_format


def fetch_nasa_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    files_count = 50
    params = {
        'count': files_count,
        'api_key': token
    }
    response = requests.get(url, params)
    response.raise_for_status()
    response = response.json()
    directory = 'nasa_apod_images'
    os.makedirs(directory, exist_ok=True)
    for index, image in enumerate(response, start=1):
        image_url = image['url']
        if get_file_format(image_url) == '.jpg':
            response = requests.get(image_url)
            response.raise_for_status()
            file_name = f'nasa_apod_{index}.jpg'
            writing_file(directory, file_name, response)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(nasa_api_key)
