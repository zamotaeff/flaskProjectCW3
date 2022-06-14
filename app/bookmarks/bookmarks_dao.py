import os
import json

from app.posts.posts_dao import PostDAO


PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

posts_dao = PostDAO(PATH)


class BookmarksDAO:

    def __init__(self, path):
        """Задаем абсолютный путь
        для загрузки файла с данными"""
        self.path = path

    def __len__(self):
        return len(self.load_data())

    def load_data(self):
        """Загружаем данные из json файла
        и отдаем список"""
        with open(self.path + '../../data/bookmarks.json', encoding='utf-8') as file:
            bookmarks_data = json.load(file)

        return bookmarks_data

    def save_data(self, data):
        """Сохраняем полученные данные в файл json"""
        with open(self.path + '../../data/bookmarks.json', mode='w', encoding='utf-8') as file:
            json.dump(data, file)

    def get_posts_data(self):
        """Получаем данные с постами по их ID,
        используем функцию map для создания списка,
        который отдаем"""
        post_ids = self.load_data()

        posts = [post for post in map(posts_dao.get_by_pk, post_ids)]

        return posts

    def add(self, post_id):
        """Добавляем ID от поста в закладки"""
        post_ids = self.load_data()

        if post_id not in post_ids:
            post_ids.append(post_id)
            self.save_data(post_ids)

    def delete(self, post_id):
        """Удаляем ID поста из закладок"""
        post_ids = self.load_data()
        post_ids.remove(post_id)
        self.save_data(post_ids)
