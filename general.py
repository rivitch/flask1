# файл app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # создается папка instance
db = SQLAlchemy()
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')   
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

# Создание таблиц базы данных
# @app._got_first_request
# def create_tables():
#     with app.app_context():
#         db.create_all()

# @app._got_first_request
# def create_tables():
#     db.create_all()

'''
@app.before_first_request
AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: '_got_first_request'?
@app._got_first_request
TypeError: 'bool' object is not callable
'''


if __name__ == "__main__":
    app.run(debug=True)
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
return f'User({self.username}, {self.email})' # вывод инфы о пользователе

@app.before_first_request
def create_tables():
db.create_all()

@app.route('/')
def index():
return 'Привет'

if __name__ == "__main__":
app.run(debug=True)
```

В этом коде мы добавили декоратор `before_first_request` перед функцией `create_tables()`, чтобы гарантировать, что вызов `db.create_all()` будет происходить перед первым запросом к приложению.

Теперь база данных будет инициализироваться в контексте вашего приложения и не должно возникать ошибки "Working outside of application context".

'''