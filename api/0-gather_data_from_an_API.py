#!/usr/bin/python3
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
user_id = sys.argv[1]
r1 = requests.get(f"{url}users/{user_id}/todos")
r2 = requests.get(f"{url}users/{user_id}")
response1 = r1.json()
response2 = r2.json()
comp = 0
total = len(response1)
tasks = ""

for i in response1:
    if i["completed"]:
        comp += 1
    tasks += f"\t {i['title']}\n"
print(f"Employee {response2['name']} is done with tasks({comp}/{total})")
print(tasks, end="")
