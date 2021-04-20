import string
import random
import os

from app.base.models import BaseModel


class Article(object):
    # @TODO Создать файл config.py и переместить все константы в этот файл

    BASE_IMAGE_PATH = 'static/images/pic01.jpg'

    def __init__(self, author: str, views_count: int, title: str, text: str, id: int = None, img=BASE_IMAGE_PATH, **kwargs):
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

    def save_image(self, image):
        if image.filename:
            random_name = ''.join(
                [random.choice(string.digits + string.ascii_letters) for x in range(10)])
            img_path = f'static/images/{random_name}.jpg'
            image.save(img_path)
            if self.img is not None and self.img != self.BASE_IMAGE_PATH:
                os.remove(self.img)
            self.img = img_path
        return self.img


class Articles(BaseModel):
    pass
