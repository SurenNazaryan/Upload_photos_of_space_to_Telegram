def file_writing(directory, filename, response):
    with open(f'{directory}/{filename}', 'wb') as file:
        file.write(response.content)

