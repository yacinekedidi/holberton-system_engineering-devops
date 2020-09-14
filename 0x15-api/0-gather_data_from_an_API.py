#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1]))
    user = r.json()
    r = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = r.json()
    finished = 0
    unfinished = 0
    tasks = []
    for t in todos:
        if t.get("userId") == user.get("id") and t.get("completed"):
            finished += 1
            tasks.append(t.get("title"))
        elif t.get("userId") == user.get("id"):
            unfinished += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), finished, finished + unfinished))
    for i in tasks:
        print("\t{}".format(i))
