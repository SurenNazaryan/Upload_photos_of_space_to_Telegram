# Космический Телеграм

Проект предназначен для скачивания фотографий космической тематики сделаных таких компаниях как SpaceX и NASA, а также для публикации полученных фотографий в Telegram-канале c помощью бота.

## Как запускать скрипты и что для этого необходимо

### 1. Убедитесь, что Python установлен
Прежде чем запускать файл, убедитесь, что у вас установлен Python. Вы можете проверить это, открыв терминал или командную строку и введя:
`python --version`
или
`python3 --version`.
Если Python установлен, вы увидите версию Python. Если нет, скачайте и установите его с [официального сайта Python](https://www.python.org/downloads/).

### 2. Откройте терминал или командную строку
- **Windows**: Нажмите `Win + R`, введите `cmd` и нажмите `Enter`.
- **macOS**: Найдите "Терминал" через Spotlight (Cmd + Space).
- **Linux**: Откройте терминал через меню приложений или с помощью сочетания клавиш.

### 3. Перейдите в каталог с Python файлами
Используйте команду `cd` (change directory), чтобы перейти в каталог, где находится ваш файл. 
Пример для Windows: 
```
cd C:\Users\ВашеИмя\Documents\project
```
Пример для macOS/Linux: 
```
cd /Users/ВашеИмя/Documents/project
```
### 4. Запустите Python файл
Теперь вы можете запустить файл, используя команду `python` или `python3`, в зависимости от вашей установки. Например, если ваш файл называется `publishing_photo.py`, введите:
```
python publishing_all_photos.py
```
или
```
python3 publishing_all_photos.py
```
Если ваш файл находится в другом каталоге, вы можете указать полный путь к файлу. Например:
```
python /путь/к/вашему/файлу/publishing_all_photos.py
```
### Пример
Если у вас есть файл `publishing_all_photos.py`, находящийся в папке `Documents/project`, вы бы сделали следующее:
```
cd ~/Documents/project
```
```
python publishing_all_photos.py
```

Или, если вы на Windows:
```
cd C:\Users\ВашеИмя\Documents\project
```
```
python publishing_all_photos.py
```

После выполнения этих шагов ваш Python файл должен запуститься, и вы увидите вывод в терминале или командной строке.

## Настройка параметров окружения
В директории проекта создайте файл `.env`, откройте его с помощью блокнота и построчно впишите туда следующие параметры: 
```
NASA_API_KEY=API_ТОКЕН_NASA
```
`API_ТОКЕН_NASA` - это ваш токен для работы с API NASA. Получить этот токен можно на [сайте NASA](https://api.nasa.gov/) после заполнения неьбольшой анкеты. Токен выглядит примерно так: `FS24Pz7wJw3fMcXa1GKoKh6CJacAGPZJLJ4AJj8w`
```
CHANNEL_ID=ID_КАНАЛА
```
`ID_КАНАЛА` - это ID вашего Telegram-канала. Откройте веб версию Telegram, в разделе `Все чаты` найдите ваш канал. Скопруйте часть ссылки после символа `#`. Полученный текст и есть ID-канала. Он выглядит примерно так: `-4730435778`
```
BOT_TOKEN=ТОКЕН_БОТА
```
`ТОКЕН_БОТА` - это токен вашего Telegram-бота. Чтобы его получить, выполните команду `/token` в чате с [BotFather](https://telegram.me/BotFather). Токен выглядит примерно так: `7747985446:AAFuTe2Sm8vMEbNToAj-G60RyGtIF9amMSD`
```
PUBLICATION_FREQUENCY=ПЕРИОДИЧНОСТЬ_ПУБЛИКАЦИЙ
```
`ПЕРИОДИЧНОСТЬ_ПУБЛИКАЦИЙ` - это численное значение в секундах, указывающее на периодичность публикации фотографий. Если написать `5`, то бот будет публиковать фотографии раз в 5 секунд. Если написать `14400`, то публикация будет раз в 4 часа.

Таким образом содержание файла `.env должно выглядеть примерно так:
```
NASA_API_KEY=FS24Pz7wJw3fMcXa1GKoKh6CJacAGPZJLJ4AJj8w
CHANNEL_ID=-4730435778
BOT_TOKEN=7747985446:AAFuTe2Sm8vMEbNToAj-G60RyGtIF9amMSD
PUBLICATION_FREQUENCY=14400
```

Также необходимо установить сторонние библиотеки, не встроенные в Python и необходимые для функционирования скриптов. Для установки используется PIP. PIP — это утилита командной строки для установки, обновления и удаления сторонних библиотек. Для новых версий Python установщик пакетов Pip устанавливается автоматически вместе с интерпретатором. Запустим командную строку и проверим, что он установлен, для этого выполним команду:
```
pip --version
```
Если pip корректно установлен, то мы увидим в командной строке:
```
pip 24.3.1 from C:\Users\B-ZONE\AppData\Local\Programs\Python\Python313\Lib\site-packages\pip (python 3.13)
```
Что-то пошло не так, если:
```
"pip" не является внутренней или внешней командой, исполняемой программой или пакетным файлом.
```
Скорее всего проблема произошла во время установки Python. Удалите Python и выполните установку заново.

Если pip установлен, то можно переходить к установке библиотек. В проекте используются много сторонних библиотек, чтобы не устанавиливать отдельно каждую, можно использовать команду:
```
pip install -r requirements.txt
```
`requirements.txt` - это текстовый файл, в котором хранятся нужные библиотеки их версии.

Проверить корректность установки можно используя команду:
```
pip freeze
```
В командной строке появится список с установленными библиотеками. Откройте `requirements.txt` и убедитесь, что каждая из указанных в файле библиотек с их версиями присутвует в списке, которую вывела командная строка.

Если все вышеперечисленные рекомендации выполнены, можно переходить к запуску скриптов.

## Описание и запуск скриптов
Изначально в директории проекта присутствут папки и файлы, которые пользователю не нужно открывать, они носят технический характер и не понадобятся для работы, при этом их нельзя удалять. В этот список входят:
1. `.git`
2. `__pycache__`
3. `.gitignore`
4. `http_utils.py`
5. `working_with_files.py`

Необходимые для работы скрипты описаны ниже

### fetch_spacex_launch_images.py
Если выполнить команду:
```
python fetch_spacex_launch_images.py
```
то скрипт скачает фотографии последнего запуска ракеты SpaceX, в директории проекта создаст папку `spacex_launch_images` и сохранит там фотографии. Бывает, что фотографий на последнем запуске не делали. В такой ситуации придётся работать с другим запуском. Вот id одного из запусков, на котором делали фото: `5eb87d47ffd86e000604b38a`. Чтобы получить фотографии этого запуска по его ID, выполните команду:
```
python fetch_spacex_launch_images.py --launch_id 5eb87d47ffd86e000604b38a
```

### fetch_nasa_apod_images.py
Если выполнить команду:
```
python fetch_nasa_apod_images.py
```
то скрипт скачает 40-50 фотографий "Астрномическая картинка дня", в директории проекта создаст папку `nasa_apod_images` и сохранит там фотографии. Такой разброс количества фото связано с тем, что скрипт перебирает 50 файлов из базы данных NASA, среди которых есть такие, которые не нужны, например, файлы формата `.gif`.

### fetch_nasa_epic_images.py
Если выполнить команду:
```
python fetch_nasa_epic_images.py
```
то скрипт скачает 11 фотографий нашей планеты, в директории проекта создаст папку `earth_images` и сохранит там фотографии.

### publishing_photo.py
Если выполнить команду:
```
python publishing_photo.py nasa_apod_images
```
то Telegram-бот опубликует на канале случайную картинку из папки `nasa_apod_images`. Вместо этой папки можно указать название любой другой папки в нашем проекте, например `earth_images` или `spacex_launch_images`.

Также можно выполнить команду:
```
python publishing_photo.py nasa_apod_images --image nasa_apod_image_1.jpg
```
В таком случае опубликуется фотография c названием `nasa_apod_image_1.jpg`, которая содержится в папке `nasa_apod_images`

### publishing_photo.py
Если выполнить команду:
```
python publishing_photo.py nasa_apod_images
```
то Telegram-бот опубликует на канале поочередно все фотографии из папки `nasa_apod_images`. Как и в предыдущем скрипте, можно указать другую папку. Периодичность публикаций можно указать в файле `.env`, как уже было сказано ранее. После того, как все фотографии из папки будут опубликованы, начнется бесконечный цикл публикаций. Один цикл будет включать в себя публикацию всех фотографий папки в случайном порядке. 

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
