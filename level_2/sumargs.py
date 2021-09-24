"""Exercise 4: Create a Python function that accepts any number
 of numbers as positional arguments and prints the sum of those numbers.
"""

def sum_all(*args):
    return sum (args)

#Test cases
print(sum_all(1, 2, 27,69, 13, 27, 63, 99, 125))
print(sum_all(1, 2, 27, 27, 63, 99, 125))
print(sum_all(1, 2, 27,69, 5))
print(sum_all(1, 2, 27,69, 13))
print(sum_all(1, 2))

