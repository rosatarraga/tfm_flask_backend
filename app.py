from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dbBreastCancer import Log
from datetime import date
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:helloworld@localhost/testapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # get url
    print("alguien te llama")
    data = json.loads(request.data.decode())
    url = data["email"]
    print(url)
    # start job
    
    # return created job id
    return 'ok'

@app.route('/home', methods=['GET'])
def home():
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    log = Log('carlos', d1)
    log.save()
    return render_template('index.html')

@app.route('/breastcancer', methods=['GET'])
def breastcancer():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3113))
    app.run(debug=True, host='localhost', port=port)