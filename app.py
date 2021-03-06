"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')


@app.route('/home/', methods=["GET", "POST"])
def hello(name=None):
    if request.method == "POST":
        name = str(request.form["name"])
        if name:
            return render_template('index.html', name=name)
        else:
            return render_template('home.html', error=True)
    return render_template('home.html', error=None, name=name)

@app.route('/home/index')
def index():
    return render_template('index.html', name=name)

@app.route("/nearest_mbta/", methods=["GET", "POST"])
def nearest_mbta():
    if request.method == "POST":
        location = str(request.form["location"])
        station_name, wheelchair_accessible = find_stop_near(location)

        if station_name:
            return render_template("nearest_mbta_result.html", location=location, station_name=station_name, wheelchair_accessible=wheelchair_accessible)
        else:
            return render_template("nearest_mbta_form.html", error=True)

    return render_template("nearest_mbta_form.html", error=None)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500

    

@app.route("/project_writeup/")
def project_writeup():
    return render_template('project_writeup.html')