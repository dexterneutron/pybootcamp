"""Excersise 6: Write a Python program that takes an input string from 
the user and counts the frequency of characters in the string.
"""

def char_frecuency(input_str):
    charcount = {}

    for s in input_str:
        charcount[s] = charcount[s] + 1 if s in charcount else 1

    return charcount

user_input = input("Please, write a string: ")
print(char_frecuency(user_input))