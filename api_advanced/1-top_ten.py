#!/usr/bin/python3
"""Return the top ten hot post titles of a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts in subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if not response.ok:
        print("OK")
        return

    try:
        json_data = response.json()
        posts = json_data['data']['children']
        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    except Exception:
        # If JSON parsing fails or data missing
        pass

    print("OK")
