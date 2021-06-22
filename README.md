# Python
## Why Python
- Python is a dynamically typed language

## Let's test the installation and environment
## Python Basics

- print() function is used to display outcome provided in the string
```print("Hello Raymond")```

# Variables
## Python Variables
- A variable works as a placeholder to store data
###Types of variables
- string - "anything between these " ' or this '
- integers - whole numbers
- floats - numbers with fractional values i.e 4.31

- Syntax to create a variable --> name of the variable = value of the variable
- Follow good logical naming convention
```
First_Name = "Raymond"
Last_Name  = "Mo"

# Creating a variable to store int value
Salary = 10.5 # float value
age = 19 # int value
my_age = "22" # string value

print(First_Name)
print(Last_Name)
print(Salary)
print(age)
print(my_age)
```
- type() can be used to find the type of variable
```
print(type(age)) # will print the type of variable age
print(type(my_age)) # will print the type of variable my_age
```
- input() in python is used to interact with the user - to ask user to enter required data
```
print(input("Please enter your Name "))

# Alternate way to prompt user where data can be stored
User_Name = input("Please Enter Your Name ")
print("Hello ")
print(User_Name)
```
## Activity
- variables first_name, last_name, age, DOB
- prompt user to input above value
- print/display the type of each value received from the user
- display the data back to user with greeting message
```
# Defining the variables
first_name = (input("Please enter your first name:   "))
last_name = (input("Please enter your last name:   "))
age = (int(input("Please enter your age:    ")))
DOB = (input("Please enter your Date of Birth in the format 'DD-MM-YYYY':    "))

# prompting the user for information input
print(first_name)
print(last_name)
print(age)
print(DOB)

# printing the type of each variable
print("first_name:", type(first_name), ", last_name:", type(last_name), ", age:", type(age), ", DOB:", type(DOB))

# Greeting the user with the information provided
print("Hello", first_name, last_name, "! You are", age, "and were born on", DOB)
```
## What are Data Types and Operators
### Types of Data
- Boolean - True/False, 0/1
- Numbers - 1,2,3,4,5
- Strings - A number of characters i.e "house"

##Arithmetic Operators
- '-' is used to subtract one value from another
- '+' is used to add two (or more) values
- '*' is used to multiply two (or more) values
- '/' is used to divide one value from another
- '%' is used to give the remainder of a division (modulus)
- '**' is used to give the exponential value by another value

## Comparison Operators
- '>' - Greater than
- '<' - Less Than
- '==' - Equal to
- '!=' - Not equal to
- '>=' - Is greater than or equal to
- '<=' - Is less than or equal to
```
number_1 = 4
number_2 = 2

print(number_1 + number_2) # prints the combined value of number_1 and number_2
print(number_1 - number_2) # prints the value of number_1 minus number_2
print(number_1 * number_2) # prints the product of number_1 and number_2
print(number_1 / number_2) # prints the result of number_1 divided by number_2 as a float
print(number_1 % number_2) # prints the remainder value of a division
print(number_1 ** number_2) # prints the exponential value of number_1 by number_2

# Boolean Values

print("Boolean Values")
print(number_1 <= number_2) # is number_1 less than or equal to number_2? Not True False
print(number_1 == number_2) # is number_1 equals number_2? Not True/False
print(number_1 != number_2) # is number_1 not equal to number_2? True
print(number_1 >= number_2) # is number_1 greater than number_2? True
```

# String Casting and Concatenation

Lesson objectives
- Using and Managing Strings
- String Casting
- String Concatenation
- Casting Methods

## Single and Double Quotes
```
single_quotes = 'These are single quotes and they work fine!'
double_quotes = "These are double quotes and they work fine too!"

print(single_quotes)
print(double_quotes)
```
### Adding strings together
- Use a ' ' to include a space
```
quotes = single_quotes + ' ' + double_quotes
print(quotes)
```
Or alternatively
```
print(single_quotes + ' ' + double_quotes)
```
## Concatenation
```
First_Name = 'James'
Last_Name = 'Bond'
age = 42

print(First_Name)
print(Last_Name)

print(First_Name + ' ' + Last_Name)
print(First_Name + ' ' + Last_Name +  ' ' + str(age), "years old")
```
## String Slicing and Indexing

- In Python Indexing starts with 0
```
           #0123456789....
greeting = "Hello World!"
                      #-1
```
- len() can be used to determine the length of the string
```
print(len(greeting))
```
- Slicing the string from index 0 to 4 up to (not including) 5, from left to right
```
print(greeting[0:5])
```
- Slicing the string from index -1, from right to left
```
print(greeting[-1])
```

- For just the string "World!"
```
print(greeting[6:])
```
Or Alternatively
```
print(greeting[-6:])
```
## String Built-In Methods

### Removing White Spaces
```
white_spaces = "Example of white spaces:                        "
print(len(white_spaces)) # len() counts white spaces as well as characters
print(white_spaces + " including white spaces")
```
- strip() can be used to remove white spaces
```
print(len(white_spaces.strip()))
print(white_spaces.strip() + " without white spaces")
```

```
example_text = "here's loads of text in a TEXT string"
```

- count() finds the number of times a specific string appears in a variable

```print(example_text.count("text"))```

- lower() converts all characters into lower case

```print(example_text.lower())```

- upper() converts all characters into upper case

```print(example_text.upper())```

- capitalize() is used to capitalize the first letter of the string

```print(example_text.capitalize())```

- replace() is used to change a specific string from within the larger one

```print(example_text.replace("loads", "plenty"))```