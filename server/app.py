from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    return '<iframe src="https://viewer.millicast.com?streamId=Kb4XjT/s" allowfullscreen width="640" height="480"></iframe>'
