from flask import Blueprint, redirect, request, render_template
import io
import os
import json
from PIL import Image
from flask.helpers import url_for
from . import model


handlers = Blueprint("handlers", __name__)

@handlers.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file found" #redirect("/upload")#request.url)
        file = request.files["file"]
        if not file:
            return "No image found"

        extension = file.filename.split(".")[-1]
        file.save(f"website/static/images/prediction.{extension}")
        predict_image = Image.open(f"website/static/images/prediction.{extension}")
        results = model(predict_image)  # includes NMS

        results.print()
        results.save('website/static/images')

        confidence = results.pandas().xyxy[0]["confidence"].to_frame() * 100
        confidence_val = round(confidence["confidence"][0], 2)


        # return redirect(url_for("views.upload", data={"confidence":confidence_val, "prediction":f"images/prediction.{extension}"}))
        return render_template("upload_image.html", data={"confidence":confidence_val, "prediction":f"images/prediction.{extension}"})