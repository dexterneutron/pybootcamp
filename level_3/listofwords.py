"""Exercise 4: Write a Python function using list comprehension
 that receives a list of words and returns a list that contains:
-The number of characters in each word if the word has 3 or more characters
-The string “x” if the word has fewer than 3 characters
"""

def list_of_words(wordlist):
    output = [len(word) if len(word) >= 3 else "x" for word in wordlist]
    return output

#Test case

words = ["foo", "bar", "baz", "qux", "quux", "corge", "gr",
 "garply", "waldo", "f", "plugh", "x", "thud"]
words_output = list_of_words(words)

print(f"""Input List: {words}
Output List {words_output}""")