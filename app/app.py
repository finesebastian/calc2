"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/home")
def home():
    """Home Route Response"""
    return render_template('home.html')
