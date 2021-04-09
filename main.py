from flask import Flask, render_template, abort, request, redirect, session
import random
import string
import os
from app.users.controller import UserController

app = Flask(__name__)

app.secret_key = 'asdasdasdasd'

BASE_IMG_PATH = 'static/images/pic01.jpg'
articles = [
    {
        'id': 1,
        'author': 'Petro Petrovich',
        'views_count': 0,
        'img': BASE_IMG_PATH,
        'title': 'Hello world!',
        'text': 'Hello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqwe'
    },
    {
        'id': 2,
        'author': 'Ivan Ivanovich',
        'title': 'World Hello',
        'img': BASE_IMG_PATH,
        'views_count': 0,
        'text': 'World HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld Hello'
    }
]


@app.route('/')
def main_page():
    if 'email' not in session:
        return redirect('/register')
    return render_template('index.html', title='ItStep Blog', articles=articles)





if __name__ == '__main__':
    user = UserController(app)
    app.run(host='localhost', port=5000)
