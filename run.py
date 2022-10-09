import os

from flask import Flask

# Импортируем блюпринт
from app.db import db
from app.posts.routes import posts_blueprint
from app.posts.routes_api import posts_api_blueprint
from app.bookmarks.routes import bookmarks_blueprint

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

# Создаем экземпляр Flask
app = Flask(__name__)

app.config.from_pyfile('config/production.py')

# SQL
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'

# регистрируем первый блюпринт
app.register_blueprint(posts_blueprint)
app.register_blueprint(posts_api_blueprint)
app.register_blueprint(bookmarks_blueprint)

db.init_app(app)

# Запускаем сервер только, если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run(
        debug=app.config.get("FLASK_DEBUG"),
        host=app.config.get("HOST"),
        port=app.config.get("PORT")
    )
