#!/usr/bin/python3
"""
0. How many Subs?
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers in a
    Subreddit
    If the subreddit is not valid returns 0
    """
    headers = {'User-Agent': 'About Page : SubscriberCount /Reddit'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if 'application/json' in \
       response.headers.get('content-type', ''):
        return response.json()['data'].get("subscribers", 0)
    return 0
