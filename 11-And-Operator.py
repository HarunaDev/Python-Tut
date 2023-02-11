# and - and operator only evaluates the second arguement if the first one is a truthy value. e.g;

print(0 and 1) #0  
print(1 and 0) #0
print(False and "hey") #False
print("hi" and "hey") #"hey"
print([] and False) #[]
print(False and []) #False

# To pass the test on this challenge, you are to analyze the following logical statements and provide your answer as an inline comment.

# Edit code below this line
{} and 4
"False" and []
0 and False
"False" and True
0 and 5
-4 and "True"
# Edit code above this line