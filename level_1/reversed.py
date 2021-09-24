"""Exercise 2: Write a Python program that accepts the user's
first and last name and prints them in reverse order with a space between them."""

first_name = input("What's your first name?")
last_name = input("What's your last name?")

print(f"{first_name[ :: -1]} {last_name[ :: -1]}")