import os
import numpy as np
from information_retrieval import retrieve_information, upload_file
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_cors import CORS
import time

# Used for uploading files
UPLOAD_FOLDER = '../uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'html'}
app = Flask(__name__, template_folder = '../templates', static_folder = None)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(os.path.join(app.config["UPLOAD_FOLDER"]), exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# SHOW FILE CONTENT
@app.route('/file/<filename>', methods=['GET'])
def show_file(filename):
    if request.method == 'GET':
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# SEARCH PAGE
@app.route('/searched/<query>', methods=['POST', 'GET'])
def searched(query):
    retrieved = ""
    if request.method == 'GET':
        retrieved = retrieve_information(query)
    return {"data" : retrieved} , 200

# UPLOAD FILE
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    time.sleep(4)
    print(request.files)
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file selected")
            return redirect(request.url)

        # uploaded_files = flask.request.files.getlist("file[]")
        file = request.files['file']
        fileToUpload = request.files['file_1']
        if file.filename == '':
            print("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # To get the current timestamp

            now = datetime.now()
            filename = secure_filename(file.filename)
            timestamp = datetime.timestamp(now)
            new_name = str(timestamp) + "_" + filename


            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            # if not firstSuccess :
            #     print("second")
            upload_file(fileToUpload,new_name, file.filename)

            # Rename file name
            # os.rename(r'../uploads/' + filename, r'../uploads/' + new_name)
            # if filename in os.path.join(app.config['UPLOAD_FOLDER']):
            #     try:

            #     except:
            #         print('Something was wrong')
            return {"message" : "File successfully uploaded!"} , 200

if __name__ == '__main__':
    app.run(debug=True)
