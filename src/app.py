import os
import numpy as np
from information_retrieval import retrieve_information
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

# Used for uploading files
UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'html'}
app = Flask(__name__, template_folder = '../templates', static_folder = None)
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
    if request.method == 'POST':
        retrieved = retrieve_information(query)
        # print(retrieved)
        # if query !='':
            # return redirect(url_for('searched', name = query))
    return {"test" : retrieved} , 200
    # return test.json()

# UPLOAD FILE
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file selected")
            return redirect(request.url)

        # uploaded_files = flask.request.files.getlist("file[]")
        file = request.files['file']
        if file.filename == '':
            print("No file selected")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # if filename in os.path.join(app.config['UPLOAD_FOLDER']):
            #     try:
                    
            #     except:
            #         print('Something was wrong')      
            return {"iya" : "halo"} , 200

if __name__ == '__main__':
    app.run(debug=True)