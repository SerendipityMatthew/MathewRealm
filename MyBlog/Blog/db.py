import pymysql
import click
from flask import current_app, g
from flask.cli import with_appcontext

USER_NAME = 'xuwanjin'
PASSWORD = 'Mathew@1991'
HOST_ADDRESS = '127.0.0.1'
PORT = 3306
CHARSET = 'utf8'
db = 'blog_db'


def get_db():
    if 'db' not in g:
        g.db = pymysql.Connect(
            host=HOST_ADDRESS,
            user=USER_NAME,
            port=PORT,
            password=PASSWORD,
            database=db,
            charset=CHARSET
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('Blog/MySql/insert_article.sql') as f:
        sql = f.read().decode('utf8')
        sql_list = sql.split(';')
        del sql_list[len(sql_list) - 1 ]
        for s in sql_list:
            d = s + ';'
            print(d)
            db.cursor().execute(d)
        f.close()
    


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")
