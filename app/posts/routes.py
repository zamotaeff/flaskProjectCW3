import os

from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from app.posts.posts_dao import PostDAO
from app.comments.comments_dao import CommentDAO
from app.bookmarks.routes import BookmarksDAO

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

posts_dao = PostDAO(PATH)
comments_dao = CommentDAO(PATH)
bookmarks_dao = BookmarksDAO(PATH)

posts_blueprint = Blueprint('posts_blueprint', __name__)


@posts_blueprint.route('/')
def page_index():
    """Главная страница с постами,
    в шаблон передаем все посты и кол-во закладок"""

    return render_template('index.html',
                           items=posts_dao.get_all(),
                           bookmarks=len(bookmarks_dao))


@posts_blueprint.route('/posts/<int:pk>/')
def page_post(pk):
    """Страница рендерит шаблон конкретного поста по его ID"""

    try:
        select_post = posts_dao.get_by_pk(pk)
        post_tags = posts_dao.get_post_tags(pk)
        select_comments = comments_dao.get_all_by_post_id(select_post.pk)

        return render_template('post.html',
                               item=select_post,
                               sub_items=select_comments,
                               tags=post_tags)

    except ValueError:
        abort(404)


@posts_blueprint.route('/search/', methods=['GET', 'POST'])
def page_search():
    """Страница поиска постов"""

    if request.method == 'POST':
        query = request.form.get('q')

        if query:
            found_posts = posts_dao.search(query)
            return render_template('search.html', items=found_posts)
        else:
            return render_template('search.html')
    elif request.method == 'GET':
        return render_template('search.html')


@posts_blueprint.route('/users/<username>/')
def page_user_feed(username):
    """Страница с постами определенного пользователя"""
    try:
        user_posts = posts_dao.get_all_by_user_name(username)

        return render_template('user-feed.html', items=user_posts)

    except ValueError as error:
        abort(404)


@posts_blueprint.route('/tags/<tag>/')
def page_tag_feed(tag):
    """Страница с постами,
    которые содержат заданный тег"""
    try:
        posts_by_tag = posts_dao.get_posts_by_tag(tag)

        return render_template('tag.html', items=posts_by_tag, tag=tag)

    except ValueError as error:
        abort(404)
