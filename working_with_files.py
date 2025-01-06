import os


def file_writing(directory, filename, response):
    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)


def get_file_format(url):
    file_format = os.path.splitext(url)[1]
    return file_format


def get_file_size_in_mb(directory, file_name):
    file_size_in_b = os.path.getsize(f'{directory}/{file_name}')
    file_size_in_mb = file_size_in_b / B_IN_MB
    return file_size_in_mb


def true_file_size(directory, file_name):
    file_size_in_mb = get_file_size_in_mb(directory, file_name)
    return file_size_in_mb < TG_FILE_SIZE_LIMIT_IN_MB
