# файл app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # для подключения к базе данных SQLite
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # создается папка instance
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)  # добавление
    def __repr__(self):
        return f'User({self.username}, {self.email})'  #вывод инфы о  пользователе

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Post({self.title}, {self.content})'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'Comment({self.content})' 

@app.cli.command("init-db")# Создание таблиц в базе данных
def init_db():
    db.create_all()
    print('OK')  
# В терминале flask init-db  - создается Бд в пакпке instance     

@app.cli.command("add-john")#1. Создание записей (34:15)
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)    # пользователь в кэше но не записан
    db.session.commit()     # пользователь записан в бд
    print('John add in DB!')
# В терминале flask add-john  - создается запись в БД  
# 
@app.cli.command("edit-john")#  Изменение записей
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')
# В терминале flask edit-john  - Изменение записи в БД

#  Удаление записей
@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)  #  Удаление записей
    db.session.commit()     # пользователь удален из бд  
    print('Delete John from DB!')  
# В терминале flask del-john  - Удаление записей в БД

#  Наполнение тестовыми данными
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}',
        email=f'user{user}@mail.ru')
        db.session.add(new_user)  # добавлено 5 новых пользователей
    db.session.commit()           # все добавлены за 1 раз
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
