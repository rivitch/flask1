# Работа с данными
# 1. Создание записей (34:15)

from flask import Flask, render_template
from models_05 import db , User#, Post, Comment

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../mydatabase.db' # запуск не через консоль, не через wsgi, а напрямую из этого 
                                                                        #файла вызвать add.run. 2 точки - выйти на уровень вверх, т.е из
                                                                        # папки instance, следующие 2 - корень проекта, и уже там будет 
                                                                        # каталог instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')# через route можно добавлять непосредственно с сайта!!!!! 
def index():
    return 'Привет'

@app.route('/data')# через route можно добавлять непосредственно с сайта!!!!! 
def data():
    return 'Ваши данные' 

@app.route('/users/') 
def all_users():
    users = User.query.all() # all выбираем всех
    context = {'users': users,}
    return render_template('users.html', **context) 

if __name__ == "__main__":
    app.run(debug=True)
