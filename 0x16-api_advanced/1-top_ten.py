#!/usr/bin/python3
"""function"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "yacinekedidi"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        r = response.json()
        info = r.get("data")
        children = info.get("children")
        for post in children:
            title = post.get("data").get("title")
            print(title)
