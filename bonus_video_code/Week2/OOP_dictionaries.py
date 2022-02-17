# List of modules for Python: https://docs.python.org/3/py-modindex.html

# import hackathon # Import - or run - a file on the same level as this one
from classes import carrier, flight

# Create a carrier and a flight
# module_name.Class_Name (or file_name.Class_Name)
my_carrier = carrier.Carrier(2022,"Adrian's Airlines","Dojo City")
# print(my_carrier.city)

"""
Creating classes with dictionaries
"""

class Manufacturer:
    def __init__(self, data): # data = data dictionary
        self.name = data["name"] # Name of manufacturer
        self.hq_city = data["hq_city"] # City where it's based
        self.year_founded = data["year_founded"]
        self.cars = [] # Empty list holding Cars

    def add_cars(self, data_list): # data_list = List of car dictionaries
        # Looping through the list of car dictionaries
        for this_car_dictionary in data_list:
            # Create a Car
            car_instance = Car(this_car_dictionary)
            # Link this Car to this Manufacturer
            self.cars.append(car_instance)
        return self

class Car:
    def __init__(self, data):
        self.model_name = data["model_name"]
        self.doors = data["doors"]


list_of_manufacturer_dictionaries = [
    {
        "name": "Chevrolet",
        "hq_city": "Detroit",
        "year_founded": 1940
    },
    {
        "name": "Toyota",
        "hq_city": "Tokyo",
        "year_founded": 1920
    },
]

list_of_manufacturer_class_instances = []

# Create a list of Manufacturer instances by going through each dictionary
for manufacturer_dictionary in list_of_manufacturer_dictionaries:
    # print(manufacturer_dictionary)
    manufacturer_class_instance = Manufacturer(manufacturer_dictionary) # Create a class of Manufacturer
    list_of_manufacturer_class_instances.append(manufacturer_class_instance)

# Loop through the manufacturer class instances to show that it works
for this_manufacturer_instance in list_of_manufacturer_class_instances:
    print(this_manufacturer_instance.name)

list_of_chevys = [
    {
        "model_name": "Corvette",
        "doors": 2,
    },
    {
        "model_name": "Malibu",
        "doors": 4,
    },
]

# Add two cars to the Chevrolet manufacturer
chevy_instance = list_of_manufacturer_class_instances[0]
chevy_instance.add_cars(list_of_chevys)

# Loop through the cars for Chevrolet - show their names
for car in chevy_instance.cars:
    print(car.model_name)


""" 
Creating class instances from within using class methods
"""
class Performer:
    all_performers = [] # Class variables holding all Performers

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        # self.created_at = data["created_at"]
        # self.updated_at = data["updated_at"]

    @classmethod
    def create_performers(cls, data_list):
        for performer_dictionary in data_list:
            performer_class_instance = cls(performer_dictionary) # Creates an instance of the class you're in - cls() is like Performer()
            cls.all_performers.append(performer_class_instance)

performer_list = [
    {
        "id": 1,
        "name": "Leonardo Dicaprio",
    },
    {
        "id": 2,
        "name": "Linda Hamilton",
    },
]

Performer.create_performers(performer_list)

# Loop through the instances of Performers
for this_performer in Performer.all_performers:
    print(this_performer.name)