from flask import render_template, request, redirect, abort
import random
import string
import os

from app.articles.models import *


class ArticleController:

    def get_one_article(self, id: int):
        return next(iter(filter(lambda x: x.id == id, self.articles.items)))

    def save_image(self, image, old_path=None):
        # @TODO Вынести в файл articles.models.Article
        if image.filename:
            random_name = ''.join(
                [random.choice(string.digits + string.ascii_letters) for x in range(10)])
            img_path = f'static/images/{random_name}.jpg'
            image.save(img_path)
            if old_path is not None:
                os.remove(old_path)
        else:
            img_path = BASE_IMG_PATH
        return img_path

    def __init__(self, app):
        self.app = app
        self.articles = Articles('../../database/articles.json', Article)

        @app.route('/article/<int:id>')
        def get_article(id):
            article = self.get_one_article(id)
            if article is None:
                abort(404)
            article.add_view()
            return render_template('article.html', article=article)

        @app.route('/create/article', methods=['GET', 'POST'])
        def create_article():
            if request.method == 'GET':
                return render_template('create_article.html')
            elif request.method == 'POST':
                self.articles.push(Article(**{
                    'id': self.articles.get_last_id(),
                    'author': request.form['article_author'],
                    'title': request.form['article_title'],
                    'img': self.save_image(request.files['article_image']),
                    'views_count': 0,
                    'text': request.form['article_text'],
                }))
                return redirect('/')
            else:
                return 'METHOD NOT ALLOWED'

        @app.route('/update/article/<int:id>', methods=['GET', 'POST'])
        def update_article(id):
            article = self.get_one_article(id)
            if article is None:
                abort(404)
            if request.method == 'GET':
                return render_template('update_article.html', article=article)
            elif request.method == 'POST':
                article.title = request.form['article_title']
                article.author = request.form['article_author']
                article.text = request.form['article_text']
                article.img = self.save_image(request.files['article_image'], old_path=article['img'])
                return redirect(f'/article/{article["id"]}')

