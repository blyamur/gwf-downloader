import requests
import os
import re

def download_fonts(url):
    while True:
        if url == '':
            url = input('Paste the link and press Enter / Вставьте ссылку и нажмите Enter: ')
        else:
            break
    # Создаем папку для скачивания файлов, если она не существует
    # Create a folder for downloading files if it does not exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # Открываем ссылку и получаем содержимое файла
    # Open the link and get the contents of the file
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
    content = response.text
    # Выводим в консоль содержимое ссылки
    # Output the contents of the link to the console
    print(content)
    # Ищем все ссылки на файлы со шрифтами
    # Find all links to font files
    pattern = r'src: url\((.*?)\) format\(\'woff2\'\);'
    matches = re.findall(pattern, content)

    total_files = len(matches)
    for i, match in enumerate(matches, start=1):
        # Получаем ссылку на файл
        # Get a link to the file
        file_url = match.strip('\'"')
        # Получаем имя файла
        # Get the file name
        file_name = file_url.split('/')[-1]

        # Скачиваем файл
        # Download the file into the directory
        response = requests.get(file_url)
        with open('downloads/' + file_name, 'wb') as file:
            file.write(response.content)

        # Выводим информацию о скачивании
        # Display download information
        print(f"Download {i} from {total_files}: {file_url}")
    print("Готово | Done!")
# Вводим ссылку с клавиатуры
# Input the link from the keyboard
url = input("Paste the link and press Enter / Вставьте ссылку и нажмите Enter: ")
download_fonts(url)
