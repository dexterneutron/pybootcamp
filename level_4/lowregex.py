""" Exercise 1 Write a Python regex function to find sequences
of lowercase letters joined with an underscore.
"""

import re

def match_regex(input_str):
    regex = '^[a-z]+_[a-z]+$'

    if(result := re.search(regex, input_str)):
        return "Match found!", result
    return "Not a Match"


#Test Cases

print(match_regex("a_b"))
print(match_regex("aaaa_bbbb"))
print(match_regex("AA_BB"))
print(match_regex("AaA_BbB"))