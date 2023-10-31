# Шаблонизатор Jinja
# 2. Условный оператор в шаблоне
"""
<p>К прочтению предлагается {{ number }}
    {% if number == 1 %}
        пост
    {% elif 2 <= number <= 4 %}
        поста
    {% else %}
        постов
    {% endif %}  # обязательно закрытие блока if
</p
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')         # главная страница
def index():         
    return 'Привет!'


@app.route('/if/')
def show_if():
    context = {'title': 'Ветвление',
            'user': 'Кто-то',
            'number': 1
    }
    return render_template('show_if.html', **context)

if __name__ == "__main__":
    app.run()#(debug=True)