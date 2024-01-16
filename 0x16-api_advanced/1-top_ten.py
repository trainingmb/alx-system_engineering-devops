#!/usr/bin/python3
"""
1. Top Ten
"""
import requests


def top_ten(subreddit):
    """
    Quearies Reddit API and prints the titles of
    the first 10 hot posts listed in the given subreddit
    """
    headers = {'User-Agent': 'Hot Top ten /Reddit'}
    payload = {'count': '10',
               'limit': '25'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=payload)
    if 'application/json' in \
       response.headers.get('content-type', ''):
        data = response.json()['data']['children']
        for child in [data[i] for i in range(10)]:
            print(child.get('data', {}).get('title'))
    else:
        print(None)
