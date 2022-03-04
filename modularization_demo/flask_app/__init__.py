from flask import Flask
app = Flask(__name__) # Create the app itself

# Session and later on flash messages
app.secret_key = "my_secret_key"