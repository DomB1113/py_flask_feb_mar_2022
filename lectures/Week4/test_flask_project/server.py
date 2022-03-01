from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # Equivalent to localhost:5000 (or technically localhost:5000/)

def animal_home_page():
    name = "Nathan"
    list_of_animals = [
        "Tiger",
        "Kangaroo",
        "Sloth",
        "Penguin",
        "Giraffe",
        "Orangutan",
        "Otter",
        "Hippo",
        "Elephant"
    ]
    return render_template("animals.html", some_name = name, animals = list_of_animals)

# Route to show animal name using a path variable
@app.route("/zoo/<animal_name>") # Equivalent to localhost:5000/zoo/<animal name> - notice the path variable
def one_animal_page(animal_name): # Don't forget the parameter!
    return render_template("one_animal.html", name = animal_name)

if __name__=="__main__": 
    app.run(debug=True)

