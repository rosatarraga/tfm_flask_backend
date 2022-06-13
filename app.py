import os
import json
import base64
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dbBreastCancer import Logs
from datetime import date
from subprocess import run, PIPE
from io import BytesIO
from PIL import Image
app = Flask(__name__)

#database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # get url
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
    img.save('breast_model/sample_data/images/1', "png")

    print("completado")
    # start job --> modify with the image to be saved
    p = run("run_single.sh 'sample_data/images/2_R_MLO.png' 'R-MLO' ", stdout=PIPE, stderr=PIPE, cwd="breast_model", shell = True)
    print( 'exit status:', p.returncode )
    print( 'stdout:', p.stdout.decode() )
    print( 'stderr:', p.stderr.decode() )
    # p = run( [ 'echo', 'hello' ], stdout=PIPE, stderr=PIPE, shell = True)

    # print( 'exit status:', p.returncode )
    # print( 'stdout:', p.stdout.decode() )
    # print( 'stderr:', p.stderr.decode() )
    # return created job id
    return 'ok'

def logUser(email):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    log = Logs(email, d1)
    log.save()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3113))
    app.run(debug=True, host='0.0.0.0', port=port)