import os
import pytest

from app.posts.posts_dao import PostDAO

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

posts_dao = PostDAO(PATH)


class TestPostsDAO:

    def test_get_all(self):

        assert posts_dao.get_all() == 8, 'Ошибка получения всех постов'

    def test_get_post_by_pk(self):

        user_post = posts_dao.get_by_pk(1)

        assert user_post.poster_name == 'leo', 'Ошибка в получении имени'

    def test_search(self):

        found_posts = posts_dao.search('раньше')

        assert len(found_posts) == 2, 'Ошибка при поисковом запросе'

    def test_get_all_by_user_name(self):

        user_post = posts_dao.get_all_by_user_name('leo')

        assert len(user_post) == 2, 'Ошибка получения постов пользователя по имени'
