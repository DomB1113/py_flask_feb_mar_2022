# Useful site for basic algorithms, loops, etc.: https://edabit.com/

my_list = [2, 8, 4, 9, 7, 15]

# One way to loop - with indexes (or indices)
for x in range(len(my_list)): # range(6) -> 0, 1, 2, 3, 4, 5
    print(my_list[x]) # NOT print(x)

for y in my_list: # y = 2, 8, 4, 9, 7, 15 - so the actual value itself
    print(y)

some_dictionary = {
    "name": "Adrian",
    "number": 88,
    "state": "Washington",
}

print(some_dictionary)

# One way to print the values
for value in some_dictionary.values():
    print(value)

# Another way - using the keys and values directly
for this_key, this_value in some_dictionary.items():
    print(f"{this_key}: {this_value}")

# A third way - using .keys()
for this_key in some_dictionary.keys(): # this_key: "name", "number", "state"
    # print(some_dictionary[this_key])
    # print(this_key)
    print(f"{this_key}: {some_dictionary[this_key]}")
    # dictionary['key'] # Access a value in a dictionary
    # some_dictionary['name']

# A fourth way - without using .keys(), .values() or .items()
for x in some_dictionary: # x = current key, so "name", "number" or "state"
    # print(some_dictionary[x])
    print(f"{x}: {some_dictionary[x]}")