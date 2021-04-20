"""Модели для проекта flask_introduction"""
import json
import sqlite3

from app.base.models import BaseModel


class UserRole:
    ADMIN = '2'
    USER = '1'
    GUEST = '0'


class User(object):

    def __init__(self, email, password, role=UserRole.GUEST, id=None, username=None, **kwargs):
        self.id = id
        self.username = username
        self.email = email
        self.role = role
        self.password = password

    @staticmethod
    def keys():
        return 'id', 'username', 'email', 'role', 'password'

    def __dict__(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
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

    def __init__(self):
        self.db = sqlite3.connect('blog.db', check_same_thread=False)
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id integer not null primary key,
                    username text,
                    email text not null unique,
                    password text not null,
                    role text not null
                )
                """)
        self.db.commit()

    def create_user(self, user: User):
        dict_user = user.__dict__()
        dict_user.pop('id')
        self.cursor.execute(f"""
        INSERT INTO users ({ ', '.join(dict_user.keys()) }) 
        VALUES ({ ', '.join([f'"{x}"' for x in dict_user.values()]) })
        """)

        self.db.commit()

    def get_all_users(self):
        keys = User.keys()
        self.cursor.execute(f"""
            SELECT {', '.join([x for x in keys])} FROM users
        """)
        users = self.cursor.fetchall()
        users_dict = [dict(zip(keys, x)) for x in users]
        return [User(**x) for x in users_dict]

    def find_one(self, id: int):
        keys = User.keys()
        self.cursor.execute(f"""
        SELECT {', '.join([x for x in keys])} from users where id = {id}
        """)
        user = self.cursor.fetchone()
        dict_user = dict(zip(keys, user))
        return User(**dict_user)

    def remove(self, id: int):
        self.cursor.execute(f"""
        DELETE FROM users WHERE id = {id}
        """)
        self.db.commit()



