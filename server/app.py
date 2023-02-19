from flask import Flask, render_template, request

from dolby import *
from db import *
from helpers import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<iframe src="{stream_url("s")}" allowfullscreen width="640" height="480"></iframe>'

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route("/stream/<label>")
def stream(label=None):
    if label is None:
        return "invalid label"
    
    name = cur.execute("SELECT name FROM streams ").fetchall()
    if name is None:
        return f"stream with label {label} does not exist"

    return f'<iframe src="{stream_url(name)}" allowfullscreen width="640" height="480"></iframe>'

@app.route("/form", methods=["GET", "POST"])
def publish():
    if request.method == "GET":
        return render_template("form.html")

    name = request.form["title"]
    label = generate_label() 
    description = request.form["description"]
    recipient = request.form["recipient"]
    goal = request.form["goal"]

    print(name, label, description, recipient, goal)

    response = publish_token(name, label)
    if response["status"] == "fail":
        return "authentication error"

    insert_row(response["data"]["id"],
               name,
               label, 
               description,
               recipient,
               goal,
               response["data"]["token"])

    print(cur.execute("SELECT * FROM streams").fetchall())

    return f"{name}/{response['data']['token']}"

"""
@app.route("/donate", methods=["POST"])
def donate(user=None):
    if user is None:
        return "please supply a user" 
"""
