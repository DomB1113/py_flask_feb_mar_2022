class Flight:
    def __init__(self, number, starting_city, ending_city):
        self.number = number
        self.starting_city = starting_city
        self.ending_city = ending_city
        self.carrier = None # Placeholder that will hold a Carrier for this Flight