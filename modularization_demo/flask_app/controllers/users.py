from flask_app import app
from flask import render_template, redirect, request, session
# Import your models

@app.route("/") # Equivalent to localhost:5000 (or 127.0.0.1)
def index():
    # Usually interact with your models
    # Either return a file (render_template) or redirect (POST requests, CREATE, UPDATE, DELETE)
    return render_template("main.html")