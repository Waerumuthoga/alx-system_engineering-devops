#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit.
"""


def number_of_subscribers(subreddit):
    """
    If an invalid subreddit is given, the function should return 0.
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
	data = response.json()
	subscribers = data['data']['subscribers']
        return subscribers
    else:
	return 0
