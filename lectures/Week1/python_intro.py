x = "First string"
y = "Second string"
print(x + y) # Prints "First stringSecond string"
print(x + " " + y) # Whenever you use the "+", you MUST insert spaces yourself
print(x, y) # If you use commas, the spaces will automatically be inserted for you

z = 25000
print(f'The value of z is {z}')

"""
This is a multi-line
comment here.
"""

x2 = """
Hello world
This is another line
"""

print(x2)

# Tuple and list demo
tuple_1 = (1, 3, 8)
list_1 = [1, 3, 8]

# How can I change the 1 to a 5 in list_1?
list_1[0] = 5
print(list_1)
print(tuple_1[1])

# How would I add the value 10 to the end of list_1?
list_1.append(10)
print(list_1)

# tuple_1[0] = 5 # TypeError - can't change a tuple's values

# Demo of dictionaries
this_dictionary = {
    "name": "Adrian",
    "number": 88,
    "my_list": ["Math", "Coding"],
}

print(this_dictionary["name"])