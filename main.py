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
    return render_template('index.html', title='ItStep Blog', articles=article.articles.items)


if __name__ == '__main__':
    user = UserController(app)
    article = ArticleController(app)
    app.run(host='localhost', port=5000)
