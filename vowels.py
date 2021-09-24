"""Excercise 1: Write a Python program to test whether a passed letter is a vowel or not."""

def vowels(vowel):
    return True if vowel.lower() in {"a","e","i","o","u"} else False

#Testing cases
print(vowels("a"))
print(vowels("u"))
print(vowels("E"))
print(vowels("I"))
print(vowels("o"))
print(vowels("r"))
print(vowels("s"))
print(vowels("y"))
print(vowels("z")) 