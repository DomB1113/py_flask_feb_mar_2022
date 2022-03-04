from flask_app import app
from flask_app.controllers import carriers, flights # IMPORTANT: import ALL your controllers!

# Run the app here
if __name__=="__main__":
    app.run(debug=True)