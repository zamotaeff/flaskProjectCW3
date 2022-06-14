import json
import logging
import os

PATH = os.path.dirname(os.path.realpath(__file__)) + '/'

logging.basicConfig(
    filename=PATH + "../api.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class PostAPIDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружаем данные из json файла
        и отдаем список с данными о постах"""
        with open(self.path + '../../data/posts.json', encoding='utf-8') as file:
            posts_data = json.load(file)

        return posts_data

    def get_all(self):
        """Получаем все посты
        без какой либо фильтрации, обработки"""
        posts = self.load_data()
        # логируем обращение
        logger.info(f'Запрос /api/posts/')

        return posts

    def check_post_exist(self, post_id):
        """Проверяем существует ли пост по его ID"""
        all_posts = self.load_data()

        for post in all_posts:
            if post['pk'] == post_id:
                return post_id

        raise ValueError

    def get_by_pk(self, pk):
        """Получаем данные поста по его ID"""
        posts = self.load_data()

        self.check_post_exist(pk)
        # логируем обращение
        logger.info(f'Запрос /api/posts/{pk}')

        for post in posts:
            if post['pk'] == pk:
                return post
