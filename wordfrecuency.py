"""Excersise 5: Write a Python program to count the 
frequency of words in a text file.
"""

TEXTFILE = "loremipsum.txt"

def count_frecuency(textfile):
    text_file = open(TEXTFILE, "r")
    words_dic = {}

    for line in text_file:
        words = line.split()
        
        for w in words:
            word = w.strip(""".,;:()[]}{^`¡!´´°?¿-_@""").lower()
            if word in words_dic:
                words_dic[word] += 1
            else:
                words_dic[word] = 1

    text_file.close()

    return words_dic

print(count_frecuency(TEXTFILE))

