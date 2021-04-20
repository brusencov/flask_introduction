from flask import Flask, render_template, redirect, session
import sqlite3

from app.users.controller import UserController
from app.articles.controller import ArticleController

app = Flask(__name__)

app.secret_key = 'asdasdasdasd'


@app.route('/')
def main_page():
    if 'email' not in session:
        return redirect('/register')
    # @TODO Создать для модели Articles функцию get_all_articles() - которая будет возвращать все статьи из базы
    return render_template('index.html', title='ItStep Blog', articles=article.articles.items)


if __name__ == '__main__':
    user = UserController(app)
    article = ArticleController(app)
    app.run(host='localhost', port=5000)


"""
Задание #1: Создать для модели Articles функцию get_all_articles() - которая будет возвращать все статьи из базы
Задание #2: Добавить в модели Articles возможность получить одну статью по ид из БД
Задание #3: Добавить в модель Articles функцию create_articles - которая будет добавлять в базу новую статью
Задание #4: Добавить функцию в модель Articles которая будет обновлять статью по ид
Задание #5: Научить контроллер article работать с моделью Articles
"""

