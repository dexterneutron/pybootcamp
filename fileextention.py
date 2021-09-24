"""Excersise 3: Write a Python program that accepts a filename from the user 
and prints the filename’s extension.."""

filename = input("What's the filename?")
extension = filename.split(".")[-1]

print(extension)