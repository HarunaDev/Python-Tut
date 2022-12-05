# Variables - We can create a new variable by assigning a value to a label e.g are as follows;

name = "Alvin"
age = 32
likes_food = True
eatsRice = False 

# Variables can't start with a number and variable names should not be followed with special characters, it's best you use the nnaming convention above when declaring your variables.

# You can't use a keyword when naming variables, keywords are words that have specific meanings in python e.g are for, if, while, import, and, True, False etc.

# Expressions, Statements & Programs in python - 

# an Expression is any type of code in python that returns a value e.g 
1 + 1
"Haruna"

# a Statement is an operation on a value, e.g are;
 
greet = "Hello, world!"
print(greet)  

# a Program is formed by a series of statement like we have above. But those statements can be put in one line but must be separated by a semi-colon e.g;

greet_two = "Hello, pythonistas!"; print(greet_two)

# Comments - In the python language or program, anything after a hashtag is completely ignored, e.g;

# this is a commented line.
4 + 4 # this is an inline comment

# Programmers use comments to make code inactive and also pass messages in their programs to other developers who might be reading their code.  

# Indentation - Every line of code indented belongs only to the block of code that it is indented within, it is important to know that indentation is very important in python.

# Data Types - Python has several built in types ranging from strings, numbers, booleans etc. You can check for the type of a data using the type() function. e.g;

typeCheck = "What data type is this?"
print(type(typeCheck))
print(isinstance(typeCheck, str))

# in the example above, we are checking if the type of the variable and in the other print statement we are coomparing if the variable type is a string using the isinstance() function.

# Python automatically knows the type of data being stored, but you can also create a variable of a specific type using the class constructor by passing the value or a variable name. it can also be used to convert data types e.g;

ageCheck = float("32")
print(isinstance(ageCheck, float)) 
print(ageCheck) 

# below are some data types and how to check them

# complex for complex numbers
# bool for booleans
# list for list
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# Operators - (Assignment, Arithmetic, Comparison, Boolean/Logical, Bitwise, is & in)

# Assignment Operator - The assignment operator allows us to assign a value to a variable or a vaariable value to another variable eg;

number_one = 1
number_two = number_one + 1

# Arithmetic Operator - They allow us to carry out mathematics expressions in our program eg;

1 + 1 #addition
2 - 1 #subtraction
2 * 2 #multiplication
4 / 2 #division
4 % 3 #modulus (remainder)
4 ** 2 #to the power
5 // 2 #floor division

# we can use the addition operator to concatenate string values. e.g;

greeting = "Hello," + " " + "Alvin"
print(greeting)

# we can also combine arithmetic operators with the assignment operators. eg;

bamodu_age = 13
bamodu_age += 12 # bamodu_age = bamodu_age + 12 
print(bamodu_age)

# Comparison Operators - We use the comparison operator to compare between different data. e.g;

a = 2
b = 1

a == b #False
a != b #True
a > b #True
a <= b #False

# Boolean Operators - Boolean operators are also logical operators, to check if a statement is truthy or falsey. there are only a few of them which are shown in the examples below;

condition1 = True
condition2 = False

not condition1 #False - checking if it is "not" true
condition1 and condition2 #False - checking if the first "and" second are true, they both have to be true.
condition1 or condition2 #True - checking if either the first "or" the second are true

# or - or operator usually returns the expression of the first operand that is a truthy value, e.g;

print(0 or 1) #1
print(False or "hey") #"hey"
print("hi" or "hey") #"hi"
print([] or False) #False
print(False or []) #[]

# and - and operator only evaluates the second arguement if the first one is a truthy value. e.g;

print(0 and 1) #0
print(1 and 0) #0
print(False and "hey") #False
print("hi" and "hey") #"hey"
print([] and False) #[]
print(False and []) #False

# Bitwise Operators - they are rarely used but it's good to know what they represent just in case you run into a situation to use them. eg;

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# is & in -

# is - also called the identity operator, it's used to compare two objects and return true if both are the same object

# in - also called the membership operator, it's used to tell if a value is contained in a list or a sequence

# Ternary Operator - It helps you to quickly define a conditional, below is an example of a conditional using if/else statement and a faster way using the ternary operator.

# using if/else
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
print(is_adult(20))

# using ternary operator
def is_adult2(age):
    return True if age > 18 else False
print(is_adult2(20))

# Strings - A string is a set of characters enclosed in double or single quotes, as long as the quotes are the same on both sides. e.g;

string_one = "double quote string"
string_two = "single quote string"
string_example = "please always use " + string_one + "s when coding."
string_example += " ;)"
print(string_example)

# It is good to know that you can make strings multi-line when you enclose them in three quotes on each side e.g;

print("""this 
        is a multi-line
        string """)

