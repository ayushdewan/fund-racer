from flask import Flask, render_template, request, redirect, url_for, jsonify

from dolby import *
from db import *
from helpers import *
from checkbook import *

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return f'<iframe src="{stream_url("s")}" allowfullscreen width="640" height="480"></iframe>'

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/stream/<label>")
def stream(label=None):
    if label is None:
        return "invalid label"
   
    name = cur.execute(f"SELECT name FROM streams WHERE label='{label}'").fetchall()
    if len(name) == 0:
        return f"stream with label {label} does not exist"
    print(name)
    name = name[0][0]
    url = stream_url(name)

    goal = cur.execute(f"SELECT goal FROM streams WHERE label='{label}'").fetchall()[0][0]

    return render_template("stream.html", url=url, goal=goal, label=label)
    # return f'<iframe src="{stream_url(name)}" allowfullscreen width="640" height="480"></iframe>'

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
    return redirect(url_for('success',label=label, name=name, response=response["data"]["id"]))

@app.route('/success/<label>/<name>/<response>')
def success(label, name, response):
    #f"http://127.0.0.1:5000/stream/{label}"
    return render_template("success.html", label=label, name=name, response=response)

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route("/donate", methods=["POST"])
def donate():
    data = request.json
    label = data["label"]
    print("ALBEL: ", label)
    org = cur.execute(f"SELECT recipient FROM streams WHERE label='{label}'").fetchall()[0][0]
    response = make_payment(data["amount"], org)
    print(response)
    return jsonify(img_uri=response["image_uri"])
