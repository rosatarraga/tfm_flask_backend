from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000), unique=False, nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, date):
        print (name,date)
        self.name = name
        self.date = date
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit() 
