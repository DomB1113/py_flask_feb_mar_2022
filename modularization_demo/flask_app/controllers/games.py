from flask_app import app
from flask import render_template, redirect, request, session
# Import your models
# from flask_app.models import game, user
@app.route("/games")
def all_games():
    # Usually interact with your models
    # Either return a file (render_template) or redirect (POST requests, CREATE, UPDATE, DELETE)
    return render_template("my_games.html")