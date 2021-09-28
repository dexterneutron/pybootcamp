"""Exercise 6: Write a python file with two functions: a function that receives a number and
appends to a global variable list, and another function that returns this list ordered.
"""

def append_global(number):
    globals()[str(number)] = number

def print_global():
    print(dict(sorted(globals().items())))

#Test Cases
append_global(3)
print_global()

append_global(5)
print_global()

append_global(6)
print_global()


