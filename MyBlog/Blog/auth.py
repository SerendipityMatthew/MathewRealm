import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from Blog.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db = get_db()
        error = list()
        if not username:
            error.extend('Username is required')
        if not password:
            error.extend('Password is required')
        if not email:
            error.extend('Email is required')
        if len(error) >= 1:
            raise RuntimeError
        cursor = db.cursor().execute("CREATE DATABASE IF NOT EXISTS blog_user_db;")
        from flask.cli import current_app 
        with current_app.open_resource("MySql/insert_user.sql") as f:
            sql = f.read().decode('utf8').split(';')
            del sql[len(sql)-1]
            db.cursor().execute(
                sql[0]
            )
        user_query = db.cursor().execute(
            'SELECT id FROM user WHERE username = {}'.format(username)).fetchone()
        email_query = db.cursor().execute(
            'SELECT id FROM user WHERE email = {}'.format(email)).fetchone()
        if error is None:
            db.cursor().execute(
                'INSERT INTO user (username, password) VALUES (?, ?)', (
                    username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.cursor().execute(
            'SELECT * FROM user WHERE username = {}'.format(username)
        ).fetchone()
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wraped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wraped_view

