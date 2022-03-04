from flask_app.config.mysqlconnection import connectToMySQL # Allow us to connect to MySQL
# Might need to import your app in the future:
# from flask_app import app

# Import other models as needed:
# from flask_app.models import flight # Create Flights by doing flight.Flight()

class Carrier:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.hq_city = data['hq_city']
        self.year_founded = data['year_founded']
        self.total_workers = data['total_workers']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.flights = [] # Placeholder holding MANY Flights linked to this Carrier - to be done in Wednesday's lecture

    # Use classmethods to interact with our database - where our queries will go