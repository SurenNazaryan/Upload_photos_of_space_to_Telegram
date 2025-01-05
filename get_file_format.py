import os


def get_file_format(url):
    file_format = os.path.splitext(url)[1]
    return file_format

