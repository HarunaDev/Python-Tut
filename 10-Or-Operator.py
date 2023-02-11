# or - or operator usually returns the expression of the first operand that is a truthy value, e.g;

print(0 or 1)  #1 0 is a falsey value, hence it will return 1

print(False or "hey")  #"hey"  False is a falsey value, hence it will return "hey"

print("hi" or "hey")  #"hi"  "hi" is a truthy value

print([] or False)  #False  [] is a falsey value, hence it will return False which is also a falsey value

print(False or [])  #[]  False is a falsey value, hence it will return [] which is also a falsey value

# To pass the test on this challenge, you are to analyze the following logical statements and provide your answer as an inline comment.

# Edit code below this line
"alvin" or []
1 or 20
False or "lfgc"
{} or 2022
False or ""
# Edit code above this line