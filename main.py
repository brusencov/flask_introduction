from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html', title='ItStep Blog')


@app.route('/about')
def about_page():
    return 'About page!'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
