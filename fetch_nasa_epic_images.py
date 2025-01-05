import requests
import os
from dotenv import load_dotenv
from file_writing import file_writing
from http_utils import fetch_response, fetch_response_data


def get_earth_image_url(image_date_time, image_name, image_format):
    base_url = 'https://api.nasa.gov/EPIC/archive/natural?api_key=DEMO_KEY'
    split_url = base_url.split('?', maxsplit=1)
    request_path = split_url[0]
    request_parameters = split_url[1]
    image_date = ('/').join(image_date_time.split(' ')[0].split('-'))
    image_file = image_name + image_format
    new_request_path = []
    new_request_path.extend([
        request_path,
        image_date,
        image_format[1:],
        image_file
    ])
    earth_image_url = '?'.join([
        '/'.join(new_request_path),
        request_parameters
    ])
    return earth_image_url


def fetch_earth_images(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': token}
    response_data = fetch_response_data(url, params)
    directory = 'earth_images'
    image_format = '.png'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for index, image in enumerate(response_data, start=1):
        image_date_time = image['date']
        image_name = image['image']
        earth_image_url = get_earth_image_url(
            image_date_time,
            image_name,
            image_format
        )
        response = fetch_response(earth_image_url, params=None)
        filename = f'earth_{index}{image_format}'
        file_writing(directory, filename, response)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_earth_images(nasa_api_key)
