#wsgi.py
from flask import Flask
from app import app
#from Lec3_6 import app

if __name__ == "__main__":
    app.run(debug=True)
