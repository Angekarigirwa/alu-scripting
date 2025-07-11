#!/usr/bin/python3
"""
Module to print the titles of the top ten hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.
    Prints None if the subreddit is invalid or unavailable.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:top_ten_script:v1.0 (by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post['data']['title'])
    except Exception:
        print(None)


