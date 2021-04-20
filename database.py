import sqlite3


connection = sqlite3.connect('flask.db')
cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id integer not null primary key,
                    name text,
                    email text not null unique,
                    password text not null
                )
                """)

cursor.execute("""
                INSERT INTO users (name, email, password)
                values ('Ivan', 'admin2@admin.com', 'admin1')
                """)
connection.commit()


# cursor.execute('SELECT email, password, name, id FROM users')
# users = cursor.fetchall()
# print(users)

class UserRole:
    ADMIN = '2'
    USER = '1'
    GUEST = '0'

class User:

    def __init__(self, email, password, role=UserRole.GUEST, id=None, username=None, **kwargs):
        self.id = id
        self.username = username
        self.email = email
        self.role = role
        self.password = password

    @staticmethod
    def keys():
        return ['id', 'username', 'email', 'role', 'password']

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

print(User)