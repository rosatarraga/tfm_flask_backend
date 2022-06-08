from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dbBreastCancer import Logs
from datetime import date
import json
import base64
from io import BytesIO
from PIL import Image
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

    #data = json.dumps({ 'data': request.get_json().get('email') })
    #url = data["email"]
    #print(request.json())

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # get url
    print("alguien te llama")
    data = request.form
    email = data['email']
    url = data['image']
    logUser(email)
    print(email)
    image_name = url[-10:-4] + ".png"
    if "data:image/png;base64," in url:
        base_string = url.replace("data:image/png;base64,", "")

    elif "data:image/jpeg;base64," in url:
        base_string = url.replace("data:image/jpeg;base64,", "")
    
    decoded_img = base64.b64decode(base_string)
    img = Image.open(BytesIO(decoded_img))

    file_name = image_name
    img.save(file_name, "png")

    print("completado")
    # start job
    
    # return created job id
    return 'ok'

def logUser(email):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    log = Logs(email, d1)
    log.save()

@app.route('/breastcancer', methods=['GET'])
def breastcancer():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3113))
    app.run(debug=True, host='0.0.0.0', port=port)