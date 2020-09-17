#!/usr/bin/python3
"""function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    queries the Reddit API and returns a list
    containing the titles of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "yacinekedidi"}
    params = {
              'after': after
              }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        r = response.json()
        infos = r.get("data")
        after = infos.get("after")
        for c in infos.get("children"):
            hot_list.append(c.get("data").get("title"))
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
