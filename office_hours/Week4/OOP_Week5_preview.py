class User:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.favorite_city = data["favorite_city"]
        self.movies = [] # This is an empty list holding a bunch of Movies created by the user

    def __repr__(self): # Look up __str__ vs. __repr__
        return f"User #{self.id} named {self.name}"

    @classmethod
    def some_class_method(cls):
        pass
        # INSIDE a class method: cls(this_user) - cls is for class methods; cls is like a placeholder for the class itself
        # cls(some_data) # Create an instance of the class you're in using the given dictionary called some_data

class Movie:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.release_date = data["release_date"]
        self.creator = None # User who created the Movie - will link in a different method

# List from your database (made up here for an example)
users_from_db = [
    {
        "id": 1,
        "name": "Adrian",
        "age": 50,
        "favorite_city": "Seattle"
    },
    {
        "id": 3,
        "name": "Nathan",
        "age": 30,
        "favorite_city": "Tokyo"
    },
    {
        "id": 8,
        "name": "Chris",
        "age": 25,
        "favorite_city": "San Diego"
    },
]

list_of_user_instances = [] # Hold Users after the for loop is finished
# Loop through the dictionaries to create instances of Users
for this_user in users_from_db:
    # print(this_user)
    new_user_instance = User(this_user) # Taking the current dictionary called this_user and creating an instance of the User class
    list_of_user_instances.append(new_user_instance) # Add this User to the list

print(list_of_user_instances)