import requests


def fetch_response(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response


def fetch_response_data(url, params=None):
    response = fetch_response(url, params=params)
    return response.json()
