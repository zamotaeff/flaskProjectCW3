import os
import pytest

from app.posts.posts_api_dao import PostAPIDAO

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

posts_api_dao = PostAPIDAO(PATH)

posts_dict_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


class TestPostsAPIDAO:

    def test_get_all(self):

        posts = posts_api_dao.get_all()

        assert type(posts) == list, 'Ошибка получения списка всех постов - API'
        assert list(posts[0].keys()) == posts_dict_keys, 'Ошибка ключей - API'

    def test_get_post_by_pk(self):

        user_post = posts_api_dao.get_by_pk(1)

        assert type(user_post) == dict, 'Ошибка в получении поста по ID - API'
