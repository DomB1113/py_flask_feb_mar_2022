class Vehicle:
    def __init__(self, manufacturer, doors):
        self.manufacturer = manufacturer
        self.doors = doors
    def turn_right(self):
        print("Turning right")

    def carrying_capacity(self):
        print("Vehicle can carry 20 boxes of goods")


class Truck(Vehicle): # Notice the inherited class inside the parentheses
    def __init__(self, manufacturer, doors, bed_size, gear_count):
        super().__init__(manufacturer, doors) # Use Vehicle class to create these attributes
        self.bed_size = bed_size # New attributes
        self.gear_count = gear_count

    def count_doors(self):
        return self.doors

    def carrying_capacity(self):
        # super().carrying_capacity() # Calling on the parent's carrying_capacity method
        print("Truck can carry 100 boxes of goods")

my_vehicle = Vehicle("Chevrolet", 4)
my_truck = Truck("Dodge", 4, 100, 8)

# print(my_truck.count_doors())
my_vehicle.carrying_capacity()
my_truck.carrying_capacity()

# Notice that the Truck class can use the turn_right method, even though it's not explicitly defined
my_truck.turn_right() 