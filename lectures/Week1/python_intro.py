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

"""
Wednesday lecture
"""

"""
Create a function that will receive a list with two numbers. 
Print the first value and return the second.
"""
x2 = [10, 6]
x3 = [8, 4]
def print_and_return(some_list):
    print(some_list[0])
    return some_list[1]

some_value = print_and_return(x3)
print(f"Second value: {some_value}")
# print_and_return(x3)

# Demonstration of if (conditional) statements
this_value = 100

if this_value > 70:
    print("The number is more than 70")
elif this_value > 80:
    print("This value is greater than 80")
else:
    print("This value is 70 or less")


# Find the smallest integer N such that 1 + 2 + ... + N >= 100

sum = 0
current_num = 1
while sum < 100:
    sum = sum + current_num
    print(f"Adding {current_num}")
    print(f"Total is now {sum}")
    current_num += 1

some_list = [8, 3, 4]
for k in range(len(some_list)): # k is the index: 0, 1, 2, ...
    print(some_list[k])

for val in some_list: # val is the actual value itself
    print(val) # Notice there’s no index here - the value itself is being used

def find_N(target_sum):
    sum = 0
    current_num = 0
    while sum < target_sum:
        current_num += 1
        sum = sum + current_num
        print(f"Adding {current_num}")
        print(f"Total is now {sum}")
    return current_num

print(find_N(100))
print(find_N(500))

def sum_list(some_list):
    if len(some_list) == 0: # Empty list
        return 0
    else:
        total = 0 # Start off with 0
        for i in range(len(some_list)): # Loop through list
            total += some_list[i] # Add current item
        return total # Return cumulative sum

print(x2)
print(sum_list(x2))

x = [
    {"id": 1, "name": "Melissa"},
    {"id": 3, "name": "Adrian"},
    {"id": 6, "name": "John"},
]

# VERSION 1
for curr_dictionary in x:
    print(curr_dictionary)
    # WARNING: Don’t mix quotation marks up - you have to use two different types below
    print(f'Person #{curr_dictionary["id"]} is {curr_dictionary["name"]}')

# # VERSION 2
for i in range(len(x)):
    curr_dictionary = x[i] # Create a variable that holds the current dictionary
    # print(curr_dictionary)
    # WARNING: Don’t mix quotation marks up - you have to use two different types below
    print(f'Person #{curr_dictionary["id"]} is {curr_dictionary["name"]}')

# VERSION 3 (similar to 2)
for i in range(len(x)):
    # print(x) # ENTIRE list of dictionaries
    # print(x[i]) # Current dictionary at index i
    # print(x[i]["id"]) # Print id
    # print(x[i]["name"]) # Print name
    print(f'Person #{x[i]["id"]} is {x[i]["name"]}')