from flask import Flask, render_template, abort

app = Flask(__name__)
articles = [
    {
        'id': 1,
        'author': 'Petro Petrovich',
        'title': 'Hello world!',
        'text': 'Hello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqweHello world weqeqweqwe'
    },
    {
        'id': 2,
        'author': 'Ivan Ivanovich',
        'title': 'World Hello',
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
            return render_template('generic.html', article=article)
    abort(404)


@app.route('/create/article')
def create_article():
    pass


data = """
<div class="content">

    <p>{{ article['text'] }}</p>

</div>
"""

data.find('{{')
args = "article['text']"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
