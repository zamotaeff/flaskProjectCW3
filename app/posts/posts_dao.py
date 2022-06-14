import json

from .post import Post


class PostDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружаем данные из json файла
        и создаем список объектов класса Post"""
        with open(self.path + '../../data/posts.json', encoding='utf-8') as file:
            posts_data = json.load(file)
            posts = []

            for post in posts_data:
                p = Post(post['poster_name'],
                         post['poster_avatar'],
                         post['pic'],
                         post['content'],
                         post['views_count'],
                         post['likes_count'],
                         post['pk'])

                posts.append(p)

        return posts

    def get_all(self):
        """Получаем все посты без какой-либо фильтрации"""
        posts = self.load_data()

        return posts

    def check_username_exist(self, username):
        """Проверяем существует ли такое имя автора поста"""
        all_posts = self.load_data()

        for post in all_posts:
            if post.poster_name.lower() == username.lower():
                return username

        raise ValueError

    def check_post_exist(self, post_id):
        """Проверяем существует ли пост с таким ID"""
        all_posts = self.load_data()

        for post in all_posts:
            if post.pk == post_id:
                return post_id

        raise ValueError

    def get_all_by_user_name(self, user_name):
        """Получаем все посты
        определенного автора по его имени"""
        all_posts = self.get_all()

        self.check_username_exist(user_name)

        user_posts = [post for post in all_posts if post.poster_name == user_name]

        return user_posts

    def get_by_pk(self, pk):
        """Получаем конкретный пост по его ID"""
        posts = self.load_data()

        self.check_post_exist(pk)

        for post in posts:
            if post.pk == pk:
                return post

    def search(self, query):
        """Ищем пост, если находим добавляем теги в пост"""
        posts = self.load_data()
        found_posts = []

        for post in posts:
            if query.lower() in post.content.lower():
                post.tags = self.get_post_tags(post.pk)
                found_posts.append(post)

        return found_posts

    def get_post_tags(self, post_id):
        """Получаем все теги из поста по его ID"""
        post = self.get_by_pk(post_id)

        tags = [word[1:] for word in post.content.split() if word[0] == '#']

        return tags

    def get_posts_by_tag(self, tag):
        """Получаем все посты,
        где встречается запрашиваемые тег"""
        posts = self.load_data()

        found_posts = [post for post in posts if tag.lower() in self.get_post_tags(post.pk)]

        return found_posts
