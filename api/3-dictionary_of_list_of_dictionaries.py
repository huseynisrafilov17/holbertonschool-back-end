#!/usr/bin/python3
"""My API usage"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
res1 = requests.get(f"{url}users").json()
dictionary = {}
for i in res1:
    usr_id = i["id"]
    usr_name = i["username"]
    res = requests.get(f"{url}users/{usr_id}/todos").json()
    dictionary[f"{usr_id}"] = []
    for j in res:
        new_dict = {}
        new_dict["username"] = usr_name
        new_dict["task"] = j["title"]
        new_dict["completed"] = j["completed"]
        dictionary[f"{usr_id}"].append(new_dict)

with open("todo_all_employees.json", "w") as f:
    f.write(json.dumps(dictionary))
