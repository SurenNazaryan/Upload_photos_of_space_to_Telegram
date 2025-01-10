import os


def writing_file(directory, file_name, response):
    with open(f'{directory}/{file_name}', 'wb') as file:
        file.write(response.content)


def get_file_format(url):
    file_format = os.path.splitext(url)[1]
    return file_format


