# обработка URL (32:20)

from flask import Flask

app = Flask(__name__)

@app.route('/<name>/')
@app.route('/')
def hello(name='незнакомец'):   # 35:50!
    # return 'Привет, ' + name + '!' # вывод по умолчанию
    return f'Привет, {name.capitalize()}!' # Переводит name с заглавной буквы

@app.route('/file/<path:file>/')  # /file/ обязателен
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'

@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    a = str(num*(-1))   # эксперимент с выводом 
    print(type(num))             # отрицательных чисел
    return f'Передано число {num}<br/>Изменено на {a}'# \n - Выводит в одну строку, тег <br/> перевод на новую строку

if __name__ == "__main__":
    app.run(debug=True)
