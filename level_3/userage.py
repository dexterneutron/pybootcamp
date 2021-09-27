""" Exercise 3 Write a Python program that asks the user for their birth date and prints the user’s current age in years, months, and days.
Sample output: You are 25 years, 4 months, and 22 days old
"""
from datetime import datetime
from dateutil import parser

raw_bithday=input("Enter your birthday i.e (1991-5-25): \n")
try:

    birthday = parser.parse(raw_bithday)
    now = datetime.now()
    age = now-birthday
    years, remainder = divmod(age.days,365)
    months,days = divmod(remainder,30)

    print(f"""You are {years} years, {months} months and {days} days old""")

except parser.ParserError:
    print("Incorrect Format")
