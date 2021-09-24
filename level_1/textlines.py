"""Exercise 4: Write a Python program to count the number 
of lines in a text file.
"""

text_file = open("loremipsum.txt", "r")

lines = [line for line in text_file if line !="\n"]

text_file.close()

print(len(lines))