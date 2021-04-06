from flask import Flask, render_template, request, redirect, session
from models import User, Users


class UserController:

    def __init__(self, app):
        self.app = app
        self.users = Users('users.json')

        @app.route('/register', methods=['GET'])
        def register_view():
            return render_template('register.html')

        @app.route('/register/create', methods=['POST'])
        def register_new_user():
            if not self.register_validate(request.form):
                print('Валидация не пройдена')
                return redirect('/register')
            is_created = self.users.add_user(
                User(
                    id=self.users.get_last_id() + 1,
                    **request.form
                )
            )
            if not is_created:
                print('Такой юзер уже есть')
                return redirect('/register')
            self.users.save()
            session['email'] = request.form['email']
            return redirect('/')

    def register_validate(self, form):
        if not all([form.get('email'), form.get('password'), form.get('confirm_password')]):
            return False
        elif form.get('password') != form.get('confirm_password'):
            return False
        return True
