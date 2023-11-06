import secrets
from flask import Flask

app = Flask(__name__)

#str.encode(hi, encoding='utf-8')
#secrets.token_hex()
app.secret_key = str.encode(secrets.token_hex())
# a = secrets.token_hex()
# print(type(a))
# print(a)
# app.secret_key = b'd5c2b630b10685678c12027d8eda2ed375a3f36716a3171c46ac003ad3cdd25c'
print(app.secret_key, type(app.secret_key))