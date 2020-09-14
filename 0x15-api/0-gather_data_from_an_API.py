#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1]))
    user = r.json()
    r = requests.get("https://jsonplaceholder.typicode.com/todos/",
                     params={"userId": argv[1]})
    todos = r.json()
    tasks = []
    for t in todos:
        if t.get("completed"):
            tasks.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(tasks), len(todos)))
    for i in tasks:
        print("\t {}".format(i))
