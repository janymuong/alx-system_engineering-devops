#!/usr/bin/python3
'''module:
export data in JSON format for all tasks from all employees
'''
import json
import requests
from sys import argv


def export_all_tasks_to_json():
    '''write to JSON file:
    Export data in JSON format for all tasks from all employees
    '''

    api_url = 'https://jsonplaceholder.typicode.com'
    user_id = set()

    # get the list of tasks for each user and store them in a dictionary
    users_res = requests.get(f'{api_url}/users')
    users_data = users_res.json()

    tasks_by_user = {}
    for user in users_data:
        user_id.add(user['id'])
        user_tasks_res = requests.get(f"{api_url}/todos?userId={user['id']}")
        user_tasks_data = user_tasks_res.json()
        tasks_by_user[user['id']] = user_tasks_data

    # create the JSON data with the specified format
    json_data = {}
    for uid in user_id:
        json_data[str(uid)] = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for user in users_data
            if user["id"] == uid
            for task in tasks_by_user[uid]
        ]

    file_json = 'todo_all_employees.json'
    with open(file_json, 'w') as f:
        json.dump(json_data, f)


if __name__ == '__main__':
    export_all_tasks_to_json()
