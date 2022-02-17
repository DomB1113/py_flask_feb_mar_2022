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