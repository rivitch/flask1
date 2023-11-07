

from flask import Flask
#from flask_sqlalchemy import SQLAlchemy  # для подключения к базе данных SQLite 
from models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # создается папка instance

#db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def index():
    return 'Привет!'

if __name__ == "__main__":
    app.run(debug=True)