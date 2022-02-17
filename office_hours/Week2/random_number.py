"""
Demonstrating importing modules AND generating random numbers
"""

"""
Version 1
"""
# import random # Import the random module

# number_str = 'Sequence of numbers: '
# trials = 20 # Number of time we'll generate a random number
# for k in range(trials):
#     number_str += str(random.randrange(1,11))  # If you import a module, must type module_name.method_name()
#     if k != trials-1:
#         number_str += ", "
#     # print(random.randrange(1,11)) # Generate numbers one THROUGH 10, EXCLUDING 11
# print(number_str)


"""
Version 2
"""
from random import randrange # Import the method from the random module directly

number_str = 'Sequence of numbers: '
trials = 20 # Number of time we'll generate a random number
for k in range(trials):
    number_str += str(randrange(1,11)) # Now you can just write the method name only
    if k != trials-1:
        number_str += ", "
    # print(random.randrange(1,11)) # Generate numbers one THROUGH 10, EXCLUDING 11
print(number_str)