"""Модели для проекта flask_introduction"""
import json


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


class Users:

    def __init__(self, file_path):
        self.users = []
        self._file_path = file_path
        self.load()
        print(f'Загружены пользователи: {self.users}')

    def add_user(self, user: User):
        if len([x for x in self.users if user.email == x.email]) > 0:
            return False
        self.users.append(user)
        return True

    def get_last_id(self):
        return len(self.users)

    def save(self):
        f = open(self._file_path, 'w')
        users_data = json.dumps([x.__dict__() for x in self.users])
        print(f'save {users_data}')
        f.write(users_data)
        f.close()

    def load(self):
        try:
            f = open(self._file_path, 'r')
            json_data = json.loads(f.read())
            f.close()
            self.users = [User(**x) for x in json_data]
        except Exception:
            self.users = []

    def __del__(self):
        self.save()
