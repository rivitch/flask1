# Создание таблиц в базе данных
#import click
from flask import Flask
from models_05 import db , User, Post, Comment
from commands import cli

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
#app.cli.add_command(cli)

@app.route('/')
def index():
    return 'Привет'

@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным  wsgi.py
    db.create_all()
    print('OK')




if __name__ == "__main__":
    app.run(debug=True)