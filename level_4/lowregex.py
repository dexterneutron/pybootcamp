""" Exercise 1 Write a Python regex function to find sequences
of lowercase letters joined with an underscore.
"""

import re

def match_regex(input_str):
    regex = '^[a-z]+_[a-z]+$'

    if(re.search(regex, input_str)):
        return "Match found!"
    return "Not a Match"