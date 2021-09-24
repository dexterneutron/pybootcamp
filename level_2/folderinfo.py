"""Exercise 2: Write a Python program to get the size,
 permissions, owner, device, created, last modified,and last 
 accessed date time of a specified path.
"""


import os, subprocess
from datetime import datetime, timezone

def parse_shell_output(shell_output):
    parsed_output = []

    for i,val in enumerate(shell_output):
        if val == ">":
            for el in shell_output[ i+1: ]:
                if el != "\n":
                    parsed_output.append(el)
                else:
                    break
            break
    parsed_output = "".join(map(str, parsed_output)).strip(" .")
    device, user= parsed_output.split("\\")

    return device, user

FOLDER  = "test_folder"
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, FOLDER)

#As documentations says: Available options for the os.stat module, may vary depending on the OS
#In my case, Windows offers less options that Linux based systems
#this solution works for Windows systems; however this won't work
#for other OSs and I could not find a general solution that works for everyone.
# 
# After exploring different options I decided to take advantage of
# Python command line features, to execute a CMD command and parse its output 
# To get the owner and system name   

command = f'dir /q /ad "{path}" ' #this command will get folder metadata
raw_shell_output = subprocess.check_output(command, shell=True,universal_newlines=True)
device, owner = parse_shell_output(raw_shell_output)

permissions = str(oct(os.stat(path).st_mode))[-3:] #Transforms binary format to octal

created_at = os.stat(path).st_atime
created_at = datetime.fromtimestamp(created_at, tz=timezone.utc)

most_recent_access = os.stat(path).st_atime
most_recent_access = datetime.fromtimestamp(most_recent_access, tz=timezone.utc)

last_modified =  os.stat(path).st_mtime
last_modified = datetime.fromtimestamp(last_modified, tz=timezone.utc)

size = 0
for ele in os.scandir(path):
    size += os.stat(ele).st_size

print(f""" Folder Information:
    Folder: {path}
    Size: {size} Bytes
    Permissions: {permissions}
    Owner: {owner}
    Device: {device}
    Created: {created_at} UTC
    Most Recent Access: {most_recent_access} UTC
    Last Modified: {last_modified} UTC
    """)


