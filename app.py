import os
import json
import base64
from flask import Flask, render_template, request
from dbBreastCancer import createLog, returnEntries
from datetime import date
from subprocess import run, PIPE
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MAX_CONTENT_LENGTH']= 32 * 1024 * 1024
CORS(app)

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # get url
    data = request.form
    email = data['email']
    print(email)
    url = data['image']
    view = data['view']
    print(view)
    patient_id = data['patient_id']
    saveImage(url)
    benign_malign = runModel(view)
    createLog(email, patient_id, benign_malign, view)
    return 'ok'

@app.route('/results', methods=['GET'])
def results():    
    # get url
    args = request.args
    print(args.get("email"))
    json_data = returnEntries(args.get("email"))
    return json_data
    

def saveImage(url):
    if "data:image/png;base64," in url:
        base_string = url.replace("data:image/png;base64,", "")

    elif "data:image/jpeg;base64," in url:
        base_string = url.replace("data:image/jpeg;base64,", "")
    
    decoded_img = base64.b64decode(base_string)
    img = Image.open(BytesIO(decoded_img))
    img.save('breast_model/sample_data/images/test.png', "png")

def runModel(view):
    # start job --> modify with the image to be saved
    string_run =  "run_single.sh 'sample_data/images/test.png' " + view
    run(string_run, stdout=PIPE, stderr=PIPE, cwd="breast_model", shell = True)
    with open('./breast_model/json_data.json') as json_file:
        data = json.load(json_file)
        return data
    # return created job id



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3113))
    app.run(debug=True, host='0.0.0.0', port=port)

