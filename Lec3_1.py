# для подключения к базе данных SQLite 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # для подключения к базе данных SQLite

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' # создается папка instance
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/database_name'
db = SQLAlchemy(app)
...
if __name__ == "__main__":
    app.run(debug=True)