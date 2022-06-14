import os

from flask import Blueprint, jsonify
from werkzeug.exceptions import abort

from app.posts.posts_api_dao import PostAPIDAO


PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

posts_api_dao = PostAPIDAO(PATH)

posts_api_blueprint = Blueprint('posts_api_blueprint', __name__)


@posts_api_blueprint.route('/api/posts/')
def page_api_index():
    """Ендпоинт для получения всех постов, отдаем json"""

    all_posts = posts_api_dao.get_all()

    return jsonify(all_posts)


@posts_api_blueprint.route('/api/posts/<int:pk>/')
def page_api_post(pk):
    """Ендпоинт для получения json данных поста по его ID"""

    try:
        select_post = posts_api_dao.get_by_pk(pk)

        if select_post:
            return jsonify(select_post)
        else:
            abort(404)
    except ValueError:
        abort(404)
