from flask import render_template, request

from werkzeug.security import generate_password_hash
from app.forms.auth import RegisterForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data) # form.data包含客户端传过来的所有数据
        user.password = form.password.data # password属性有setter和getter
        db.session.add(user)
        db.session.commit()

    # request.form
    return render_template('auth/register.html', form={'data':{}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
