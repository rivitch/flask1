# обработка URL

from flask import Flask

app = Flask(__name__)

@app.route('/<name>/')
@app.route('/')
def hello(name='незнакомец'):
    # return 'Привет, ' + name + '!' # вывод по умолчанию
    return f'Привет, {name.capitalize()}!' # Переводит name с заглавной буквы

@app.route('/file/<path:file>/')  # /file/ обязателен
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    a = str(num*(-1))
    print(type(num))
    return f'Передано число {num}<br/>Изменено на {a}'# \n - Выводит в одну строку, тег <br/> перевод на новую строку

if __name__ == '__main__':
    app.run()
