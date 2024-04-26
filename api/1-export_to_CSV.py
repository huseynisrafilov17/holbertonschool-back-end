#!/usr/bin/python3
"""My API usage"""
import requests
import sys

if len(sys.argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    res = requests.get(f"{url}users/{user_id}/todos").json()
    res1 = requests.get(f"{url}users/{user_id}").json()
    string = ""
    user_name = res1["name"]
    for i in res:
        string += f'"{user_id}","{user_name}","{i["completed"]}","{i["title"]}"\n'

    with open(f"{user_id}.csv", "w") as f:
        f.write(string)