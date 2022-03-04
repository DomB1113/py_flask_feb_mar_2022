from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL
# Might need to import other models here
from flask_app.models import user # Import the user file -> then you can do user.User() to create a User

class Game:
    def __init__(self,data): # data is a dictionary from our database
        self.id = data['id']
        self.name = data['name']
        self.max_players = data['max_players']
        self.rating = data['rating']
        self.genre = data['genre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Don't need foreign keys here
        self.user = None # Linking one User only to a Game in terms of who created it in the database
        
    # classmethods go here to interact with the database - this is where you will interact with the database
    # AND create instances of your class

    # staticmethods to perform validations