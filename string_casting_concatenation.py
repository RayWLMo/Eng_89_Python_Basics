# Using and Managing Strings
# String Casting
# String Concatenation
# Casting Methods

# Single and Double Quotes
single_quotes = 'These are single quotes and they work fine!'
double_quotes = "These are double quotes and they work fine too!"

print(single_quotes)
print(double_quotes)

# Adding strings together
# Use a ' ' to include a space
quotes = single_quotes + ' ' + double_quotes

print(quotes)

# Or alternatively
print(single_quotes + ' ' + double_quotes)

# Concatenation
First_Name = 'James'
Last_Name = 'Bond'
age = 42

print(First_Name)
print(Last_Name)

#Combined
print(First_Name + ' ' + Last_Name)
print(First_Name + ' ' + Last_Name +  ' ' + str(age), "years old")

# String Slicing and Indexing

# In Python Indexing starts with 0
           #0123456789....
greeting = "Hello World!"
                      #-1

# len() can be used to determine the length of the string
print(len(greeting))

print(greeting[0:5])  # Slicing the string from index 0 to 4 up to (not including) 5, from left to right
print(greeting[-1])  # Slicing the string from index -1, from right to left

# For just the string "World!"
print(greeting[6:])
print(greeting[-6:])

# String Built-In Methods

# Removing White Spaces
white_spaces = "Example of white spaces:                        "
print(len(white_spaces))  # len() counts white spaces as well as characters
print(white_spaces + " including white spaces")

# strip() can be used to remove white spaces
print(len(white_spaces.strip()))
print(white_spaces.strip() + " without white spaces")

# Other Built-In Methods

example_text = "here's loads of text in a TEXT string"

# count() finds the number of times a specific string appears in a variable
print(example_text.count("text"))

# lower() converts all characters into lower case
print(example_text.lower())

# upper() converts all characters into upper case
print(example_text.upper())

# capitalize() is used to capitalise the first letter of the string
print(example_text.capitalize())

# replace() is used to change a specific string from within the larger one
print(example_text.replace("loads", "plenty"))
