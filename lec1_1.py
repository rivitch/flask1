# import flask
from flask import Flask

# app = flask.Flask(__name__)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello wsgi.py!'
    # return 42   # ошибка, возвращается только строковое представление

if __name__ == "__main__":
    app.run(debug=True)

# flask --app .\lec11_1.py run (21:00) # - в VSC не работает
"""
PS F:\GB\TASKS\flask1> flask --app  .\lec1_1.py run
flask : Имя "flask" не распознано как имя командлета, функции, файла сценария или выполняемой программы. Проверьте правильность написания имени, а также наличие и правильность пути, после чего повторите попытку.
строка:1 знак:1
+ flask --app  .\lec1_1.py run
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (flask:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
"""
# ввод через cmd с правами администратора - не работает
"""
F:\GB\TASKS\flask1>flask --app  .\lec1_1.py run
"flask" не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.
"""