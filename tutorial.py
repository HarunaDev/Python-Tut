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

# Indentation - Every line of code indented belongs only to the block of code that it is indented within, it is good to know that indentation is very important in python.
# The colon character (:) is used to specify Indentation.

option = input()
if option == "Lead-Forte":
    print("I go to school here!")
else:
    print("Sorry, I didn't get it")

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

# String Methods - You can perform certain operations or methods on that string. e.g;

print("alvin".upper()) # to make all characters uppercase
print("ALVIN".lower()) # to make all characters lowercase
print("ALVIN hARUNA".title()) # to make the first letter of a word uppercase
print("ALVIN".islower()) # to check if the string is in lowercase, it'll return either True or False


# It is important to know that string methods only returns a new string and doesn't mutate the original string. e.g;

string_method = "check this out"
print(string_method.title())
print(string_method)

print(len(string_method)) # you can use some global functions on a string, len() can be used to check for the length of characters in the string
print( "eck" in string_method) # using the in operator to check if a string contains a sub string

# Strings - Escaping Characters -- You can also escape certain character's in python using the back-slash \ before the cheracter you want to escape, what it means is that when you escape a character, it won't function as it normally would in python, but rather it becomes part of a string. e.g;

escapeChar = 'Let\'s eat, Dad'

escapeChar2 = "examples of quotes you can use in python include '', \"\", and \"\"\" \"\"\" "
print(escapeChar2)

# You can also use the escape character for special formating, e.g;

print("let's make a new line \nhere and \nhere")

# String Characters & Slicing - You can also get a specific charcater in a string using square brackets e.g;

stringChar = "Hello"
print(stringChar[2]) # you can also use a  negative number to start counting at the end

# Slicing - This allows you to specify a range when trying to get a specific character. e.g;

stringChar += ", world"
print(stringChar[2:9])

# Booleans- (bool type) This data type only returns two values, either True or False e.g;

done = True

# print(type(done) == True)

if done:
    print("Yes! I'm done with my Assignment")
else:
    print("No, I'm too lazy")  

# When evaluating values that are not True or False e.g other data types, it's nice to know that any value that has something is represented as True and a value with is empty will be False e'g;

checkValue = 2 #This will be True because it has a truthy value
checkValue2 = "" #This will be False because it is represented by a False value of an empty string
checkValue3 = -1 #This will be true because a negative value represents a truthy value

# Global functions with booleans in python

# any() - This can be used to check if any of the arguements or data passed into it is True, it'll return True if one of the data is a truthy value. e.g;

book_1_read = True
book_2_read = False

read_any_book = any(book_1_read, book_2_read)
print(read_any_book)

# all() - This function is similar to the any() function except that it only returns True when all the data passed into it are of a truthy value. e.g;

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all(ingredients_purchased, meal_cooked)
print(ready_to_serve)
