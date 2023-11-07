# Работа с данными
# 1. Создание записей (34:15)

from flask import Flask
from models_05 import db , User, Post, Comment
#from commands import cli

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
#app.cli.add_command(cli) # инициализация через командную строку

@app.route('/')# через route можно добавлять непосредственно с сайта!!!!! 
def index():
    return 'Привет'

@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным  wsgi.py
    db.create_all()
    print('OK')

@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)    # пользователь в кэше но не записан
    db.session.commit()     # пользователь записан в бд
    print('John add in DB!') 

@app.cli.command("edit-john")#  Изменение записей
def edit_user():
    user = User.query.filter_by(username='john').first() # формируем запрос query в таб. User с фильтрацией filter_by по имени 
                                                        #  пользователя username, найти всех john и вывести первого first
    user.email = 'new_email@example.com'  # обращаемся к ЭП объекта user и меняем ее
    db.session.commit()                  # Изменение записи user.email
    print('Edit John mail in DB!')
# В терминале flask edit-john  - Изменение записи в БД 
# 
#  Удаление записей
@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)  #  Удаление записей
    db.session.commit()     # пользователь удален из бд  
    print('Delete John from DB!')  


#  Наполнение тестовыми данными
@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}',
        email=f'user{user}@mail.ru')
        db.session.add(new_user)
        db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post %
        count + 1}').first()
        new_post = Post(title=f'Post title {post}',
        content=f'Post content {post}', author=author)
        db.session.add(new_post)
        db.session.commit()

# Получение данных из базы данных
@app.route('/users/')
    def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)
