import os
import pytest

from app.comments.comments_dao import CommentDAO

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

comments_dao = CommentDAO(PATH)


class TestCommentsDAO:

    def test_get_all_by_post_id(self):

        post_comments = comments_dao.get_all_by_post_id(1)

        assert len(post_comments) == 4, 'Ошибка получения комментариев для поста'

