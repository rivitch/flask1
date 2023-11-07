# app.py

from flask import Flask
from models_02 import db, User
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
@app.route('/')
def index():
    return 'Привет'
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')    
if __name__ == "__main__":
    app.run(debug=True)