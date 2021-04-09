"""Модели для проекта flask_introduction"""
import json
from app.base.models import BaseModel


class User(object):

    def __init__(self, id, email, password, username=None, **kwargs):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __dict__(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


class Users(BaseModel):
    pass
