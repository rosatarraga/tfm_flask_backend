import os
import json
import base64
from flask import Flask, render_template, request
from dbBreastCancer import createLog, returnEntries
from datetime import date
from subprocess import run, PIPE
from io import BytesIO
from PIL import Image
app = Flask(__name__)

#database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/dbbreastcancer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
#db = SQLAlchemy(app)

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # get url
    data = request.form
    email = data['email']
    url = data['image']
    view = data['view']
    patient_id = data['patient_id']
    saveImage(url)
    benign_malign = runModel()
    createLog(email, patient_id, benign_malign, view)
    return 'ok'

@app.route('/results')
def results():    
    # get url
    #data = request.form    
    email = "r@r.com"
    print(email)
    returnEntries(email)

def saveImage(url):
    if "data:image/png;base64," in url:
        base_string = url.replace("data:image/png;base64,", "")

    elif "data:image/jpeg;base64," in url:
        base_string = url.replace("data:image/jpeg;base64,", "")
    
    decoded_img = base64.b64decode(base_string)
    img = Image.open(BytesIO(decoded_img))
    img.save('breast_model/sample_data/images/test.png', "png")

def runModel():
    # start job --> modify with the image to be saved
    run("run_single.sh 'sample_data/images/test.png' 'R-MLO' ", stdout=PIPE, stderr=PIPE, cwd="breast_model", shell = True)
    with open('./breast_model/json_data.json') as json_file:
        data = json.load(json_file)
        return data
    # return created job id



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3113))
    app.run(debug=True, host='0.0.0.0', port=port)

