"""Exercise 5: Create a Python function that accepts 
any number of positional and keyword arguments,and that prints them back to the user. 
Your output should indicate which values were provided as positional arguments, 
and which were provided as keyword arguments.
"""

def printargs(*args, **kwargs):

    for val in args:
        print(val, "Positional Argument", sep = ", ")

    for key, el in kwargs.items():
        print(key, el, "Keyword Argument", sep = ", ")

#Test Case
print(printargs(
    "Blue",
    "Red",
    "Black",
    "Magenta",
    name = "Felix",
    lastname = "Lugo",
    profession = "Engineer"
))