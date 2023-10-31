# (22:30) создаем файл wsgi.py

from lec1_1 import app
from lec1_2 import app
from lec1_3 import app
from lec1_4 import app
from lec1_5 import app
from lec1_6 import app
from lec1_7 import app
from lec1_8 import app


if __name__ == "__main__":
    app.run(debug=True)


# flask run --debug # не работает
# РЕШЕНИЕ - 'python -m flask run --debug'