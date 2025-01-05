import requests
import os
from dotenv import load_dotenv
from get_file_format import get_file_format
from file_writing import file_writing
from http_utils import fetch_response, fetch_response_data


def fetch_nasa_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'count': 50,
        'api_key': token
    }
    response_data = fetch_response_data(url, params)
    directory = 'nasa_apod_images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for index, image in enumerate(response_data, start=1):
        image_url = image['url']
        if get_file_format(image_url) == '.jpg':
            response = fetch_response(image_url, params=None)
            filename = f'nasa_apod_image_{index}.jpg'
            file_writing(directory, filename, response)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(nasa_api_key)
