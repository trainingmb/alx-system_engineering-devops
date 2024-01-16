#!/usr/bin/python3
"""
1. Top Ten
"""
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints the titles of
    the first 10 hot posts listed in the given subreddit
    """
    headers = {'User-Agent': 'Hot Top ten /Reddit'}
    payload = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=payload)
    if 'application/json' in \
       response.headers.get('content-type', ''):
        data = response.json()['data']['children']
        for child in data:
            if not child.get('data', {}).get('locked', True) and \
               not child.get('data', {}).get('stickied', True):
                print(child.get('data', {}).get('title'))
    else:
        print(None)
