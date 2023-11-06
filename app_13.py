# Хранение данных
# 2. Создание ответа (make_response())

from flask import Flask, request, make_response, render_template


app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response
...

@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"

# @app.route('/delcookie/') # неудачный эксперимент
# def delete_cookies():
#     response = make_response(render_template('main.html', **context))
#     name = request.cookies.get('username')
#     response.delete_cookie('username', context['name'])
#     return 

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=False)
