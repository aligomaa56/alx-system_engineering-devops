#!/usr/bin/python3
"""
    given employee ID, returns information about his/her TODo list progress.
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(f"{url}/users/{employee_id }")
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    name = user_data.get('name')
    completed_tasks = []
    for task in todos_data:
        if task.get('completed'):
            completed_tasks.append(task.get('title'))
    total_tasks = len(todos_data)

    print(f"Employee {name} is done with\
         tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
