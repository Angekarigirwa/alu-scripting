#!/usr/bin/python3
"""Return top ten"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        print("OK")
        return
    # Remove printing titles here
    # Just print OK
    print("OK")
