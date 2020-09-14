#!/usr/bin/python3
""" extend your Python script to export data in the CSV format."""
import csv
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1]))
    user = r.json().get("username")

    r = requests.get("https://jsonplaceholder.typicode.com/todos/",
                     params={"userId": argv[1]})
    todos = r.json()

    with open("{}.csv".format(argv[1]), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([argv[1], user, t.get("completed"),
                             t.get("title")])
