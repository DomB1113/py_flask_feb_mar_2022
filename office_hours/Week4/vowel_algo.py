# Link to challenge: https://edabit.com/challenge/p88k8yHRPTMPt4bBo

"""
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
All test cases are one word and only contain letters.
"""

# One suggestion: count the A's, B's, C's, etc.

# Note of what the vowels are - "A", "E", "I", "O", "U" - list
# Start at the beginning of the word, then go down the line

# "Celebration", x = "C", "e", "l", etc.

def count_vowels(word): # Input - word as a string
    vowel_count = 0 # Number of vowels found in the given word
    vowel_list = ["a","e","i","o","u"]
    converted_word = word.lower() # Converts the word to all lower case
    for this_letter in converted_word: # this_letter is the current letter we're examining
        print(f"The current letter we're examining is: {this_letter}")
        # Check to see whether the current letter is in the list
        if this_letter in vowel_list:
            vowel_count += 1 # Increment vowel count by 1 since we just found a vowel
        print(f"The number of vowels so far found is {vowel_count}")
    # Output - an integer representing the number of vowels found within the word
    return vowel_count

# print(count_vowels("Celebration")) # 5
# print(count_vowels("Union")) # 3
# print(count_vowels("Strong")) # 1
# print(count_vowels("Hay")) # 1
# print(count_vowels("Adrian")) # 3

this_word = "Celebration"
print(f"The word {this_word} has {count_vowels(this_word)} vowels.")

