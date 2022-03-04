from flask_app import app # Need this to run the app itself
from flask_app.controllers import games, users # IMPORT *ALL* your controllers here!

if __name__=="__main__": # Run the app
    app.run(debug=True)