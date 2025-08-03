#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
 returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Reddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        return response.json().get("data").get("subscribers")
    