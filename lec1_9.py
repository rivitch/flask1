# Шаблонизатор Jinja
# 3. Вывод в цикле(55:00)

"""
{% for item in item_list %}
    {{ item }}
{% endfor %}
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')         # главная страница
def index():         
    return 'Привет!'


@app.route('/for/')
def show_for():
    context = {'title': 'Цикл',
            'poem': ['Вот не думал, не гадал,',
                    'Программистом взял и стал.',
                    'Хитрый знает он язык,',
                    'Он к другому не привык.',]}
    
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)

if __name__ == "__main__":
    app.run(debug=True)

# на выходе чистая страница  ??? не работает из-за отсутствия файла bootstrap.min.css
"""
127.0.0.1 - - [30/Oct/2023 16:50:10] "GET /for/ HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2023 16:50:14] "GET /for/ HTTP/1.1" 200 -
"""