#!/usr/bin/python3
"""export data in the JSON format"""
import csv
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
    with open(f"{iD}.csv", "w", newline="") as cf:
        writer = csv.writer(cf, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([iD, username, task.get('completed'),
                            task.get('title')])
