# Global functions with booleans in python

# any() - This can be used to check if any of the arguements or data passed into it is True, it'll return True if one of the data is a truthy value. e.g;

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
print(read_any_book)

# all() - This function is similar to the any() function except that it only returns True when all the data passed into it are of a truthy value. e.g;

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)

# To pass the test on this challenge, use the any & all global variables to parse through the variables declared below

got_milk = True
has_money = False
can_swim = False
can_fly = True
eats_rice = False

# Your code goes below here

# Your code goes above here