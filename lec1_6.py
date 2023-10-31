# Рендеринг HTML файла(44:00)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index/')
def html_index():
    return render_template('index1.html')  # обращение к  файлу index1.html в папке templates

if __name__ == "__main__":
    app.run(debug=True)


# не работает из-за отсутствия файла bootstrap.min.css
"""
127.0.0.1 - - [30/Oct/2023 15:18:29] "GET /index/ HTTP/1.1" 200 -
127.0.0.1 - - [30/Oct/2023 15:18:29] "GET /static/css/bootstrap.min.css HTTP/1.1" 404 -
127.0.0.1 - - [30/Oct/2023 15:18:29] "GET /static/image/Конфуций.jpeg HTTP/1.1" 404 -
"""