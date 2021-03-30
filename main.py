from flask import Flask, render_template, abort, request, redirect
import random
import string

app = Flask(__name__)
articles = [
    {
        'id': 1,
        'author': 'Petro Petrovich',
        'views_count': 0,
        'img': 'static/images/bg.jpg',
        'title': 'Hello world!',
        'text': 'Hello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqwe'
    },
    {
        'id': 2,
        'author': 'Ivan Ivanovich',
        'title': 'World Hello',
        'img': 'static/images/bg.jpg',
        'views_count': 0,
        'text': 'World HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld HelloHelloWorld Hello'
    }
]


@app.route('/')
def main_page():
    return render_template('index.html', title='ItStep Blog', articles=articles)


@app.route('/article/<int:id>')
def get_article(id):
    for article in articles:
        if article['id'] == id:
            article['views_count'] += 1
            return render_template('generic.html', article=article)
    abort(404)


@app.route('/create/article', methods=['GET', 'POST'])
def create_article():
    """
    Request methods:
        1) GET - Отвечает за получение данных
        2) POST - Отвечает за создание данных
        3) PUT - Отвечает за обновление данных
        4) DELETE - Отвечает за удаление данных
    """
    if request.method == 'GET':
        return render_template('create_article.html')
    elif request.method == 'POST':
        image = request.files['article_image']
        random_name = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(10)])
        img_path = f'static/images/{random_name}.jpg'
        image.save(img_path)
        articles.append({
            'id': len(articles) + 1,
            'author': request.form['article_author'],
            'title': request.form['article_title'],
            'img': img_path,
            'views_count': 0,
            'text': request.form['article_text'],
        })
        return redirect('/')
    else:
        return 'METHOD NOT ALLOWED'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
