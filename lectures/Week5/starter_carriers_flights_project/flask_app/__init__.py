from flask import Flask
app = Flask(__name__) # Create the app

app.secret_key = "my_secret_key" # Needed for session and flash messages (you'll learn that in week 6)
