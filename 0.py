import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(query, folder_name, num_images):
    try:
        # Создание папки для класса в текущем рабочем каталоге
        class_folder = os.path.join('dataset', folder_name)
        os.makedirs(class_folder, exist_ok=True)

        # Подготовка запроса для поиска изображений на Яндекс.Картинках
        search_url = f'https://yandex.ru/images/search?text={query}&size=large&from=tabbar'

        # Добавление параметра timeout
        response = requests.get(search_url, timeout=10)

        # Парсинг HTML-страницы с результатами поиска
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img', class_='serp-item-thumb')

        for i, img_tag in enumerate(image_tags[:num_images]):
            img_url = img_tag['src']

            # Добавление параметра timeout для избежания висения программы
            img_data = requests.get(urljoin('https:', img_url), timeout=10).content

            # Генерация имени файла с ведущими нулями
            file_name = f"{i:04d}.jpg"

            # Сохранение изображения в папку для класса
            img_path = os.path.join(class_folder, file_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    download_images('polar bear', 'polar_bear', 10)
    download_images('brown bear', 'brown_bear', 10)
