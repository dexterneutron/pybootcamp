"""Excercise 9: Write a Python function to merge two dictionaries.
"""

def merge_dicts(dict1,dict2):
    return dict1 | dict2

dict1={
    'Color' : 'Blue',
    'Name' : 'Felix',
    'Profession' : 'Engineer'
}

dict2={
    'Fav Food' : 'French Fries',
    'Fav Sport' : 'F1',
}

print(merge_dicts(dict1,dict2))