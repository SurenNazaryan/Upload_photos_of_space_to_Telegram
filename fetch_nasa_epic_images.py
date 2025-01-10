import requests
import os
from dotenv import load_dotenv
from working_with_files import writing_file
from datetime import datetime


def get_earth_image_url(image_date_string, image_name, image_format):
    url = 'https://api.nasa.gov/EPIC/archive/natural'
    dt = datetime.strptime(image_date_string, "%Y-%m-%d %H:%M:%S")
    formatted_date = dt.strftime("%Y/%m/%d")
    image_file_name = f'{image_name}{image_format}'
    new_request_path = []
    new_request_path.extend([
        url,
        formatted_date,
        image_format[1:],
        image_file_name 
    ])
    return '/'.join(new_request_path)


def fetch_earth_images(token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': token}
    response = requests.get(url, params)
    response.raise_for_status()
    response= response.json()
    directory = 'earth_images'
    image_format = '.png'
    os.makedirs(directory, exist_ok=True)
    for index, image in enumerate(response, start=1):
        image_date_string = image['date']
        image_name = image['image']
        earth_image_url = get_earth_image_url(
            image_date_string,
            image_name,
            image_format
        )
        params = {'api_key': token}
        response = requests.get(earth_image_url, params=params)
        response.raise_for_status()
        file_name = f'earth_{index}{image_format}'
        writing_file(directory, file_name, response)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    fetch_earth_images(nasa_api_key)

