"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from testgit import app
from flask import Flask,render_template,request,redirect,send_file
from werkzeug.utils import secure_filename
import time
import os
from testgit import start
from testgit import stop
@app.route('/')
@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
         return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    if request.method == 'POST':
        req = request.form
        print(req.get("City"))
        feedback = req.get("City")
        rgName = req.get("City")
        os.system('/home/site/wwwroot/TerraForm/terraform -chdir=/home/site/wwwroot/TerraForm  apply -var resourceGroupName='+rgName+ ' -auto-approve ')
        feedback = "Resource Group has been created"

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        feedback=feedback

    )



@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Group 1  contacts'
    )

@app.route('/capture', methods = ['POST', 'GET'])
def capture():
    vmList=['vm1','vm2']
    if request.method == 'GET':
         return render_template(
        'capture.html',
        vmList=vmList,
        title='Capture',
        year=datetime.now().year,
    )
    if request.method == 'POST':
        req = request.form
        print(req.get("operation"))
        operationName = req.get("operation")
        if operationName == "Start Capture":
         isCaptureStarted = start.startCapture()
         #os.system('/home/eets7302/start.py')
         feedback = "Resource Group has been created"
         return render_template(
          'capture_started.html',
           title='Capture',
           year=datetime.now().year,
           feedback=feedback
   )
        else:
          #os.system('/home/eets7302/stop.py')
          isCaptureStopped = stop.stopCapture()
          feedback = "Resource Group has been created"
          return render_template(
           'capture_stopped.html',
            title='Capture',
            year=datetime.now().year,
            feedback=feedback
   )





    """Renders the home page."""
    return render_template(
        'capture.html',
        title='Capture',
        year=datetime.now().year,
        feedback=feedback

    )

UPLOAD_FOLDER = '/home/eets7302/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Upload API
@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("saved file successfully")
      #send file name as parameter to downlad
            return redirect('/downloadfile/'+ filename)
    return render_template('upload_file.html')
# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    filename = "captures.zip"
    return render_template('download.html',value=filename)
@app.route('/return-files/<filename>')
def return_files_tut(filename):
    filename = "captures.zip"
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

