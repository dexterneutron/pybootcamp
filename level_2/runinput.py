"""Exercise 3: Write a Python program that takes user input
 and runs it as a command using the os module.
"""

import os

while True:
    user_command = input("Write a command: ")
    stream = os.popen(user_command)
    output = stream.read()
    print(output)