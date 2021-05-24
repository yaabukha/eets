"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from testgit import app
from flask import Flask,render_template,request
import time
import os
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
        time.sleep( 5 )
        os.system('/home/site/wwwroot/TerraForm/terraform -chdir=/home/site/wwwroot/TerraForm  apply -auto-approve ')
        feedback = "Resource Group has been created"
        
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        feedback=feedback
       
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


