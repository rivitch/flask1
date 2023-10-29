from flask import Flask#, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello wsgi.py!'
    # return 42   # ошибка, возвращается только строковое представление

if __name__ == '__main__':
    app.run()