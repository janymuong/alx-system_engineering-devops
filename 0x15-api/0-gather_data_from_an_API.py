#!/usr/bin/python3
'''
module: 0-gather_data_from_an_API.py
This script interacts with a RESTful API to retrieve
and display TODO list progress for a given employee ID.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
'''

import requests
import sys


def todo_progress(user_id):
    '''
    Retrieve and display TODO list progress for the specified employee.

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

        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task.get('completed'))

        print(f'Employee {employee_name} is done '
              f'with tasks({done_tasks}/{total_tasks}):')

        for task in todos_data:
            if task.get('completed'):
                print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    user_id = sys.argv[1]

    if not user_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    todo_progress(int(user_id))
