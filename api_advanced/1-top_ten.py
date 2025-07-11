#!/usr/bin/python3
"""
Module to print the titles of the top ten hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.
    If subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    except Exception:
        print(None)

