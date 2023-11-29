from distutils.log import error
import mimetypes
from urllib import request
from app import app
import io
import os
from flask import render_template, request, make_response
import requests
from elevenlabs import set_api_key, generate

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call/martha", methods = ["POST"])
def call_martha():
    set_api_key("661ac31676cb6896e2997f9973703d87")
    if request.form["text"]:
        text = request.form["text"]
        audio = generate(
            text = text,
            voice="Brian",
            model="eleven_multilingual_v2"
        )

        response = make_response(audio)
        response.headers.set("Conetnt-Type","audio/wav")
        response.headers.set("Content-Diposition","attachment",filename="audio.wav")
        return response
    else:
        return {"error": "Please provide the text"}, 400


