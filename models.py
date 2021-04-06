"""Модели для проекта flask_introduction"""
import json


class User(object):

    def __init__(self, username: str, email, phone, password, avatar):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.avatar = avatar

    def __dict__(self):
        return {
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'avatar': self.avatar
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value


class Users:

    def __init__(self, file_path):
        self.users = []
        self._file_path = file_path
        self.load()

    def add_user(self, user: User):
        self.users.append(user)

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


# users = Users('data.json')
# users.add_user(User(123,123,123,123,123))
# users.save()

