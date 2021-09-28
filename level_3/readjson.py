"""Exercise 5: Write a Python program that reads a JSON object from a file, 
sorts the object keys in ascending order, then writes the JSON object back into the file.
"""

import json
from pathlib import Path

PATH = Path(__file__).absolute().parent
file_path = PATH / "users.json"

with open(file_path, "r") as read_file:
    read_data = json.load(read_file)
read_file.close()

output_list = []
for el in read_data:
    sorted_el = sorted(el.items())
    output_list.append(dict(sorted_el))

try:
    with open(file_path, "w") as write_file:
        json.dump(output_list, write_file,indent= 4)
        print(f"Json file {file_path} have been written")
        
except Exception as e:
    print("An error has ocurred")


