from flask import Flask, request, jsonify, render_template,Response
import os
from flask_cors import CORS, cross_origin
from detector_test import Detector
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from PIL import Image
import base64
import numpy as np


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

application = Flask(__name__)
app = application
# CORS(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

UPLOAD_FOLDER = 'static'

application = Flask(__name__)
app = application

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@cross_origin()
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return "No file"
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return "File"
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            try:
                object_detector = Detector(filename)
                result = object_detector.detect_action()
                encoded_image = result['image']
            except Exception as e:
                print("The error is: ", e.with_traceback)
            else:
                return render_template('index.html', detected = encoded_image , orginal = 'static/'+filename)

if __name__ == "__main__":
    port = 5001
    application.run(host='0.0.0.0', port=port)