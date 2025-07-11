#!/usr/bin/python3
"""
Fetches and prints the titles of the top 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts from a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json_data = response.json()
    posts = json_data.get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post['data']['title'])

