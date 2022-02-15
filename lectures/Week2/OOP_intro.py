class Carrier:
    all_carriers = [] # Class variable holding all carriers
    overseer = "FAA" # Class variable

    def __init__(self, year, name, city):
        self.year = year
        self.name = name
        self.city = city
        self.flights = [] # Attribute that will hold Flights linked to this Carrier (ADDED late)
        self.total_workers = 0
        Carrier.all_carriers.append(self) # Add this Carrier to the list of all carriers

    # Examples of instance methods - notice the "self" at the start
    def print_year(self):
        print(self.year)
        return self

    def rename_airline(self, new_name):
        self.name = new_name
        return self

    def hire_worker(self):
        self.total_workers += 1
        return self

    def hire_worker_v2(self, new_hirees = 1):
        self.total_workers += new_hirees
        return self
        # cd_airlines.hire_worker_v2(3)
    
    @classmethod
    def count_carriers(cls): # Remember "cls" when making class methods!
        return len(cls.all_carriers)

# Creating two carriers

cd_airlines = Carrier(2022, "Coding Dojo Airlines", "Dojo City")
# print(cd_airlines.year)

my_airline = Carrier(2022, "Nathan's Awesome Airlines", "Torigoth")
# print(my_airline.city)

# Demonstrating instance methods and chaining
cd_airlines.print_year()
cd_airlines.rename_airline("Coding Airways")
print(cd_airlines.name)
cd_airlines.rename_airline("Programming Airlines").hire_worker().hire_worker()
print(cd_airlines.name)
print(cd_airlines.total_workers)

# Demo of class variables
third_airline = Carrier(2022, "Adrian's Airline", "Colony 9")
print(Carrier.overseer)
print(Carrier.count_carriers())

# Added Flight class
class Flight:
    def __init__(self, number, starting_city, ending_city):
        self.number = number
        self.starting_city = starting_city
        self.ending_city = ending_city
        self.carrier = None # Placeholder that will hold a Carrier for this Flight

# Creating two flights
flight_one = Flight(555, "Seattle", "Reno")
flight_two = Flight(100, "Phoenix", "London")

# IMPORTANT - adding flights to a carrier
cd_airlines.flights.append(flight_one)
cd_airlines.flights.append(flight_two)

# Show flights for this airline
for flight in cd_airlines.flights:
    print(f"{flight.starting_city} to {flight.ending_city}")

# Add carrier to a flight
flight_one.carrier = cd_airlines
print(flight_one.carrier.name) # Show name of carrier for this flight
