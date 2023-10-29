# (22:30) создаем файл wsgi.py

from lec1_1 import app

if __name__ == "__main__":
    app.run(debug=True)


# flask run --debug # не работает
# РЕШЕНИЕ - 'python -m flask run --debug'