"""Exercise 1: Write a Python program to count the number of strings 
where the string length is 2 or more and the first and last character are the same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
"""

INPUT_LIST = ['abc', 'xyz', 'aba', '1221']

count=0
for el in INPUT_LIST:
    if(el[0] == el[-1] and len (el) >= 2):
        count += 1

print(count)