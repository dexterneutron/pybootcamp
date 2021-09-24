"""Excersise 7: Write a Python function to remove duplicates from a list.
"""
#After I created this method I realized that it did't specify if
#keeping the order of the list if a requirement, so i wrote a second method
#that keeps it ordered

def remove_duplicates(lst):
    unique_lst = list(set(lst))
    
    return unique_lst

def remove_duplicates_keep_ordered(lst):
    new_list = [val for i, val in enumerate(lst) if val not in lst[:i]]

    return new_list



list_with_duplicates = [1, 1, 2, 5, 6, 777, 8, 66, 5, 99]

print(remove_duplicates(list_with_duplicates))
print(remove_duplicates_keep_ordered(list_with_duplicates))