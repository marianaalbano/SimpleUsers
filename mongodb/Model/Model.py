from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {"db":"simpleusers"}
db = MongoEngine(app)


class Users(db.Document):
    nome = db.StringField()
    telefone = db.StringField()
    endereco = db.StringField()


