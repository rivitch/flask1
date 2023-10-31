#   функции представления(view функции) (25:10)


from flask import Flask

app = Flask(__name__)

# названия функций должны различаться
@app.route('/Николай/') # последний слеш обязателен
def nike():
    return 'Привет, Николай!'
@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'
@app.route('/')         # главная страница
def index():         
    return 'Привет, незнакомец!'

if __name__ == "__main__":
    app.run(debug=True)