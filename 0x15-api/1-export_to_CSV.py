#!/usr/bin/python3
'''
module: 1-export_to_CSV.py
This script interacts with a RESTful API to retrieve
and export TODO list progress for a given employee ID in CSV format.

Usage:
    python3 1-export_to_CSV.py <employee_id>
'''

import csv
import requests
import sys


def todo_progress(user_id):
    '''
    Retrieve and export TODO list progress for the specified employee
    in CSV format.

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

        file_name = f'{employee_id}.csv'

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            for task in todos_data:
                completed_status = 'True' if task.get('completed') else 'False'
                task_title = task.get('title')
                writer.writerow([str(employee_id), employee_name,
                                 completed_status, task_title])

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
