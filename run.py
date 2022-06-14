import os

from flask import Flask

# Импортируем блюпринт
from app.posts.routes import posts_blueprint
from app.posts.routes_api import posts_api_blueprint
from app.bookmarks.routes import bookmarks_blueprint

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

# Создаем экземпляр Flask
app = Flask(__name__)

app.config.from_pyfile('config/development.py')

# регистрируем первый блюпринт
app.register_blueprint(posts_blueprint)
app.register_blueprint(posts_api_blueprint)
app.register_blueprint(bookmarks_blueprint)

# Запускаем сервер только, если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
