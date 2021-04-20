from flask import render_template, request, redirect, abort, session

from app.articles.models import *


class ArticleController:

    def get_one_article(self, id: int):
        return next(iter(filter(lambda x: x.id == id, self.articles.items)))

    def __init__(self, app):
        self.app = app
        self.articles = Articles('database/articles.json', Article)

        @app.route('/article/<int:id>')
        def get_article(id):
            # @TODO Добавить в модели Articles возможность получить одну статью по ид из БД
            article = self.get_one_article(id)
            if article is None:
                abort(404)
            article.add_view()
            self.articles.save()
            return render_template('article.html', article=article)

        @app.route('/create/article', methods=['GET', 'POST'])
        def create_article():
            if not session['role'] >= '1':
                abort(403)
            if request.method == 'GET':
                return render_template('create_article.html')
            elif request.method == 'POST':
                article = Article(**{
                    'id': self.articles.get_last_id(),
                    'author': request.form['article_author'],
                    'title': request.form['article_title'],
                    'views_count': 0,
                    'text': request.form['article_text'],
                })
                # @TODO Добавить в модель Articles функцию create_articles - которая будет добавлять в базу новую статью
                article.save_image(request.files['article_image'])
                self.articles.push(article)
                return redirect('/')
            else:
                return 'METHOD NOT ALLOWED'

        @app.route('/update/article/<int:id>', methods=['GET', 'POST'])
        def update_article(id):
            if not session['role'] >= '1':
                abort(403)
            # @TODO Добавить функцию в модель Articles которая будет обновлять статью по ид
            article = self.get_one_article(id)
            if article is None:
                abort(404)
            if request.method == 'GET':
                return render_template('update_article.html', article=article)
            elif request.method == 'POST':
                article.title = request.form['article_title']
                article.author = request.form['article_author']
                article.text = request.form['article_text']
                article.save_image(request.files['article_image'])
                return redirect(f'/article/{article["id"]}')

