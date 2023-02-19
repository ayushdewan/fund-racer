from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

streamer = {}

@app.route("/")
def hello():
    return '<iframe src="https://viewer.millicast.com?streamId=Kb4XjT/s" allowfullscreen width="640" height="480"></iframe>'

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        streamer["title"] = request.form["title"]
        streamer["description"] = request.form["description"]
        streamer["recipient"] = request.form["recipient"]
        streamer["goal"] = request.form["goal"]
        return redirect(url_for('success'))
    return render_template("form.html")


@app.route('/success')
def success():
    return render_template("success.html")


