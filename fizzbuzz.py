"""Excercise 10: Write a Python program that iterates through integers 
from 1 to 100 and prints them. For integers that are multiples of three, 
print "Fizz" instead of the number. For integers that are multiples of five, print "Buzz". 
For integers which are multiples of both three and five print, "FizzBuzz"."""

for i in range(1,101):

    if (i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)