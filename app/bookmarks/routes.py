import os

from flask import Blueprint, render_template, request, redirect
from werkzeug.exceptions import abort

from app.bookmarks.bookmarks_dao import BookmarksDAO

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

bookmarks_dao = BookmarksDAO(PATH)

# Добавил префикс для ссылок
bookmarks_blueprint = Blueprint('bookmarks_blueprint',
                                __name__,
                                url_prefix='/bookmarks')


@bookmarks_blueprint.route('/')
def page_index():
    """Главная страница с всеми закладками,
    получаем данные с постами и передаем в шаблон"""
    all_posts = bookmarks_dao.get_posts_data()

    return render_template('bookmarks.html', items=all_posts)


@bookmarks_blueprint.route('/add/<int:post_id>/')
def page_add(post_id):
    """Страница, которая принимает ID поста
     и добавляет в закладки"""
    bookmarks_dao.add(post_id)

    return redirect('/', code=302)


@bookmarks_blueprint.route('/delete/<int:post_id>/')
def page_delete(post_id):
    """Страница для удаления поста из закладок по его ID"""
    bookmarks_dao.delete(post_id)

    return redirect('/bookmarks/', code=302)
