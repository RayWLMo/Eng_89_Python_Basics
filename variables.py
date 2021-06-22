# Let's test the installation and environment

print("Hello Raymond")
# function is used to display outcome provided in the string

# Variables
# Python Variables
# Variable works as a place holder to store data
# string - "anything between these " ' or this '
# integers - whole numbers
# floats - numbers with fractional values i.e 4.31

# Syntax to create a variable --> name of the variable = value of the variable
# Follow good logical naming convention

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
# type(age) can be used to find the type of variable

print(type(age)) # will print the type of variable age
print(type(my_age)) # will print the type of variable my_age

# input() in python is used to interact with the user - to ask user to enter required data
User_Name = input("Please Enter Your Name ")
print("Hello ")
print(User_Name)

print(input("Please enter your Name "))

# Activity/task
# variables first_name, last_name, age, DOB
# prompt user to input above value
# print/display the type of each value received from the user
# then display the data back to user with greeting message

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
print("first_name is", type(first_name), ", last_name is", type(last_name), ", age is", type(age), ", DOB is", type(DOB))

# Greeting the user with the information provided
print("Hello", first_name, last_name, "! You are", age, "and were born on", DOB)
