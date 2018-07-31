from flask import (
    Blueprint, flash, g, render_template, request, url_for, redirect
)

from werkzeug.exceptions import abort
from Blog.auth import login_required
from Blog.db import get_db

bp = Blueprint('blog', __name__)





@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.fom['body']
        error = None
        if not title:
            error = 'Title is req'