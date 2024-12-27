from flask import Flask, redirect, render_template
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def index():
    return "TEST"