#!/usr/bin/python3
'''
module: 2-export_to_JSON.py
This script interacts with a RESTful API to retrieve
and export TODO list progress for a given employee ID in JSON format.

Usage:
    python3 2-export_to_JSON.py <employee_id>
'''

import json
import requests
import sys


def todo_progress(user_id):
    '''
    Retrieve and export TODO list progress for the specified employee
    in JSON format.

    Args:
        user_id (int): The ID of the employee.
    Returns:
        None
    '''

    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{user_id}'
    todos_url = f'{base_url}/todos?userId={user_id}'

    try:
        user_res = requests.get(user_url)
        todos_res = requests.get(todos_url)

        if user_res.status_code != 200 or todos_res.status_code != 200:
            print('Error: Failed to retrieve data from API.')
            sys.exit(1)

        user_data = user_res.json()
        todos_data = todos_res.json()

        employee_id = user_data.get('id')
        employee_name = user_data.get('username')

        data = {str(employee_id): []}

        for task in todos_data:
            completed_status = task.get('completed')
            task_title = task.get('title')
            data[str(employee_id)].append({
                'task': task_title,
                'completed': completed_status,
                'username': employee_name
            })

        file_name = f'{employee_id}.json'

        with open(file_name, mode='w') as json_file:
            json.dump(data, json_file)

        print(f'Data exported to {file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)


if __name__ == '__main__':
    user_id = sys.argv[1]

    if not user_id.isdigit():
        print('Error: Employee ID must be an integer.')
        sys.exit(1)

    todo_progress(int(user_id))
