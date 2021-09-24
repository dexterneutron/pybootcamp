"""Excersise 8: Write a Python function to remove an item from a tuple.
"""

def remove_from_tuple(input_tuple,element_index):
    new_tuple = tuple(el for i, el in enumerate(input_tuple) if i != element_index)
    
    return new_tuple

input_tuple = ("red", "blue", "orange", "magenta", "yellow")
output_tuple = remove_from_tuple(input_tuple, 3)

print(f"Input tuple is: {input_tuple}")
print(f"Output tuple is: {output_tuple}")

