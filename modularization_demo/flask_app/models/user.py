from flask_app import app
from flask_app.config.mysqlconnection import MySQLConnection # Allow us to connect to MySQL
# Might need to import other models here
from flask_app.models import game # Import the game file -> then you can do game.Game() to create a Game
class User:
    def __init__(self,data): # data is a dictionary from our database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.games = [] # A User can create many Games in the database
        
    # classmethods go here to interact with the database - this is where you will interact with the database
    # AND create instances of your class

    # staticmethods to perform validations