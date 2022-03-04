from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL
# Might need to import your app in the future:
# from flask_app import app

# Import other models as needed:
# from flask_app.models import carrier # Create Carriers by doing carrier.Carrier()

class Flight:
    def __init__(self, data):
        self.id = data['id']
        self.number = data['number']
        self.starting_city = data['starting_city']
        self.ending_city = data['ending_city']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Why not include carrier_id?  Because we'll link Carriers in a different way in Wednesday's lecture
        self.carrier = None # Placeholder holding ONE Carrier linked to this flight

    # Use classmethods to interact with our database - where our queries will go