""" Exercise 1: Create a simple function that fetches and parses the JSON from this API: 
https://jsonplaceholder.typicode.com/todos/ and then print all the completed TODOs in the screen.
Create a simple local web server with an API endpoint that proxies the TODOs API used above and 
accepts the "completed" and the "name" filtering. You can use any web framework you prefer.
"""

import requests
from requests.exceptions import HTTPError
def get_todos():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    try:
            response = requests.get(url)
            parsed_reponse = filter_todos(response.json())
            print(parsed_reponse)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

def filter_todos(json_input):
    new_list = []
    for el in json_input:
        if el["completed"]:
            new_list.append(el)
    return new_list

get_todos()