from flask_app import app
from flask import render_template, redirect, request, session
# Import your models
# from flask_app.models import carrier # Create Carriers by doing carrier.Carrier()

# Define our routes!  We'll define all of them in Monday's office hour!
@app.route("/")
def index():
    return redirect("/carriers")

@app.route("/carriers")
def all_carriers():
    pass