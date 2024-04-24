#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    iD = sys.argv[1]

    user_response = requests.get(f"{url}/users/{iD}")
    todos_response = requests.get(f"{url}/todos?userId={iD}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')
    data = {iD: []}
    for task in todos_data:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        data[iD].append(task_info)

    with open(f"{iD}.json", "w") as jf:
        json.dump(data, jf, indent=4)
