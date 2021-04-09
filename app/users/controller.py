from flask import render_template, request, redirect, session, abort
import random
import string

from app.users.models import User, Users


class UserController:

    def __init__(self, app):
        self.app = app
        self.users = Users('../../database/users.json', User)

        @app.route('/register', methods=['GET'])
        def register_view():
            return render_template('register.html')

        @app.route('/logout', methods=['GET'])
        def logout_user():
            if 'email' in session:
                session.pop('email')
            return redirect('/')

        @app.route('/register/create', methods=['POST'])
        def register_new_user():
            if not self.register_validate(request.form):
                print('Валидация не пройдена')
                return redirect('/register')
            is_created = self.users.push(
                User(
                    id=self.users.get_last_id() + 1,
                    **request.form
                ),
                lambda users: len([x for x in users if request.form.get('email') == x.email]) > 0
            )
            if not is_created:
                print('Такой юзер уже есть')
                return redirect('/register')
            self.users.save()
            session['email'] = request.form['email']
            return redirect('/')

        @app.route('/create/user', methods=['GET', 'POST'])
        def create_user():
            if request.method == 'GET':
                return render_template('user_form.html')
            elif request.method == 'POST':
                try:
                    if 'avatar' in request.files:
                        image = request.files['avatar']
                        random_name = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(10)])
                        img_path = f'static/images/{random_name}.jpg'
                        image.save(img_path)
                    else:
                        img_path = 'static/images/default_avatar.jpg'
                    users.append({
                        'id': len(users),
                        'username': request.form['username'],
                        'email': request.form['email'],
                        'phone': request.form['phone'],
                        'password': request.form['password'],
                        'avatar': img_path
                    })
                    return redirect('/')
                except Exception as e:
                    print(e)
                    abort(500)
            else:
                return 'METHOD NOT ALLOWED'

        @app.route('/users', methods=['GET'])
        def get_users():
            return render_template('users.html', users=users)

        @app.route('/user/<int:id>', methods=['GET'])
        def get_user(id):
            for user in users:
                if user['id'] == id:
                    return render_template('user.html', user=user)
            abort(418)

        @app.route('/delete/user/<int:id>', methods=['GET'])
        def delete_user(id):
            global users
            users = list(filter(lambda x: x['id'] != id, users))
            return 'success'

    def register_validate(self, form):
        if not all([form.get('email'), form.get('password'), form.get('confirm_password')]):
            return False
        elif form.get('password') != form.get('confirm_password'):
            return False
        return True
