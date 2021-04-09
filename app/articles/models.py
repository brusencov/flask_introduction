import json
from app.base.models import BaseModel


class Article(object):
    # @TODO Создать файл config.py и переместить все константы в этот файл

    def __init__(self, id: int, author: str, views_count: int, title: str, text: str, img='static/images/pic01.jpg', **kwargs):
        self.id = id
        self.author = author
        self.views_count = views_count
        self.title = title
        self.text = text
        self.img = img

    def __dict__(self):
        return {
            'id': self.id,
            'author': self.author,
            'views_count': self.views_count,
            'title': self.title,
            'text': self.text,
            'img': self.img,
        }

    def add_view(self):
        self.views_count += 1
        return self.views_count


class Articles(BaseModel):
    pass
