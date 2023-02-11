# Ternary Operator - It helps you to quickly define a conditional, below is an example of a conditional using if/else statement and a faster way using the ternary operator.

# using if/else statement
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
# print(is_adult(20))

# using ternary operator
def is_adult2(age):
    return True if age > 18 else False
# print(is_adult2(20))


# To pass the test on this challenge, you are to refactor the if/else statement within the function below using the ternary operator 

def fav_food(food):
    # Edit code below this line
    if food == "Rice":
        return True
    else:
        return False
    # Edit code aboove this line
print(fav_food("Rice"))