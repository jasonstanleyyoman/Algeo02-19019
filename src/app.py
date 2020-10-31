import os
import numpy as np

from information_retrieval import information_retrieval
# from ..src.information_retrieval import information_retrieval
from flask import Flask, flash, request, redirect, url_for, render_template, json
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__, template_folder='../templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

print(sum.sum1(1, 1))
dataset = np.load("../src/information_retrieval/cleared_sentence_list.npy")
# os.chdir("../src/web-scrapping")

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        query = request.form['content']
        if query !='':
            return redirect(url_for('searched', name = query))
    return render_template('home.html')

@app.route('/searched/<query>', methods=['POST', 'GET'])
def searched(query):
    if request.method == 'POST':
        
        for data in dataset: 
            temp = data.split(" ")
            print(temp[0])

        print(len(dataset))
        # print(dataset[0])
        # if query !='':
            # return redirect(url_for('searched', name = query))
    return {"test" : str(query)} , 200
    
    # return test.json()

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file selected")


        file = request.files['file']
        if file.filename == '':
            print("No file selected")


if __name__ == '__main__':
    app.run(debug=True)