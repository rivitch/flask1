#Наследование шаблонов
#Базовый и дочерние шаблоны


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')         # главная страница
def index():         
    return 'Привет!'

@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('data.html', **context)

if __name__ == "__main__":
    app.run(debug=True)