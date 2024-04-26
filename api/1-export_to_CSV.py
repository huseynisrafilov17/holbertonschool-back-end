#!/usr/bin/python3
"""My API usage"""
import requests
import sys

if len(sys.argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    usr_id = sys.argv[1]
    res = requests.get(f"{url}users/{usr_id}/todos").json()
    res1 = requests.get(f"{url}users/{usr_id}").json()
    string = ""
    usr_name = res1["name"]
    for i in res:
        string += '"{}","{}","{}","{}"\n'.format(usr_id, usr_name,
                                                 i["completed"], i["title"])

    with open(f"{usr_id}.csv", "w") as f:
        f.write(string)