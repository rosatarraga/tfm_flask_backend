from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class Logs(db.Model):
    id = db.Column(db.Integer, db.Identity(start=1, cycle=True), primary_key=True)
    email = db.Column(db.String(10000), unique=False, nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    print (email,date)
    def __init__(self, email, date):
        self.email = email
        self.date = date
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit() 

def returnEntries(email):
    result = db.session.execute('SELECT * FROM logs WHERE email = ', email)
    print (result)