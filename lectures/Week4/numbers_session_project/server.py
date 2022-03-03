from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "itsasecrettoeverybody"

# Our routes will go here
@app.route("/") # Default: methods=["GET"]
def home_page():
    return render_template("starting_page.html")

# Add user to session, then send to /numbers route
@app.route("/process_user", methods=["POST"])
def process_user():
    # print(request.form)
    session['name'] = request.form["name"] # Save name sent by the form in session
    return redirect("/numbers")

@app.route("/numbers")
def numbers_page():
    # FUTURE: Something you'll do in Week 6 onwards to check if someone is logged in
    # 'id' in session that identifies who's logged in
    # if 'id' not in session:
        # return redirect('/')
    # If there is no data for sum or numbers, create the variables
    if 'sum' not in session: # If the sum doesn't exist, we start from scratch
        session['numbers'] = []
        session['sum'] = 0
    return render_template("numbers_page.html")

# Add number to list AND sum
@app.route("/add_number", methods=["POST"])
def add_a_number():
    session['numbers'].append(int(request.form['number'])) # Add the number to the list
    session['sum'] += int(request.form['number'])
    return redirect('/numbers') # ALWAYS redirect to a route with POST requests!

# Remove sum and list of numbers
@app.route("/reset")
def reset():
    session.pop("sum", "numbers") # session.pop("variable_name") to delete variables from session
    return redirect('/numbers')

# Start all over, including with a new user
@app.route('/exit')
def exit():
    session.clear() # Clear session completely
    return redirect('/') # Send back to main page
    
if __name__=="__main__": 
    app.run(debug=True)