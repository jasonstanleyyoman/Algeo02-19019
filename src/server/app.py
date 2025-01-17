import os
from information_retrieval import retrieve_information, upload_file
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_cors import CORS
import time

# Used for uploading files
UPLOAD_FOLDER = '../../test/'
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
        ranks, term, titles = retrieve_information(query)
    return {"ranks" : ranks, "term" : term, "titles" : titles} , 200

# UPLOAD FILE
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    print(request.files)
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file selected")
            return redirect(request.url)

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
            upload_file(fileToUpload,new_name, file.filename)
            return {"message" : "File successfully uploaded!"} , 200

if __name__ == '__main__':
    app.run(debug=True)
