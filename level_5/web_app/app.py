from flask import Flask, request
from flask import render_template
import requests
from requests.exceptions import HTTPError

app = Flask(__name__)

@app.route("/")
def index():
    data = get_todos()
    user_list = [el["userId"] for el in data]
    user_list=list(set(user_list))
    return render_template('index', data = data, user_list = user_list)

@app.route("/filter", methods = ['POST'])
def filter():
    data = get_todos()
    user_id = str(request.form['user_id']).strip()  
    completed = True if 'completed' in request.form else False
    user_tasks = []
    
    for el in data:
        if str(el['userId']) == user_id:
            if (completed):
                if(el['completed']):
                    user_tasks.append(el)
            else:
                user_tasks.append(el)

    return render_template('filter', user_tasks = user_tasks)

def get_todos():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    try:
            response = requests.get(url)
            return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6