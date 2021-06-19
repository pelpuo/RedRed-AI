from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def hello():
    return render_template("index.html")

@views.route("/upload")
def upload():
    return render_template("upload_image.html")

@views.route("/capture")
def capture():
    return render_template("live_capture.html")