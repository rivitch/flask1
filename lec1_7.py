# Шаблонизатор Jinja
# 1. Пробрасываем контекст из представления в шаблон

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')         # главная страница
def index():         
    return 'Привет!'


@app.route('/index/')
def html_index():
    context = {
            'title': 'Личный блог',
            'name': 'Харитон',
    }
    return render_template('index2.html', **context)

if __name__ == "__main__":
    app.run(debug=True)