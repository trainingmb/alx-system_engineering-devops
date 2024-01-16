#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list={}):
    """
    Queries Reddit API returns a list containing
    the titles of all hot articles for a given
    subreddit.
    If no results are found for the given subreddit,
    the function should return None
    """
    headers = {'User-Agent': 'Recursive hot list /Reddit'}
    payload = {'count': 0}
    if 'after' in hot_list.keys():
        payload['after'] = hot_list['after']
        payload['count'] = hot_list['count']
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=payload)
    if 'application/json' in \
       response.headers.get('content-type', ''):
        response_json = response.json()
        data = response_json['data']['children']
        title_list = []
        for child in data:
            title_list.append(child.get('data', {}).get('title'))
        if len(title_list) == 0:
            return None
        elif response_json['data']['after'] is not None:
            rec_title_list = recurse(subreddit,
                                     {'after': response_json['data']['after'],
                                      'count': response_json['data']['dist'] +
                                      payload['count']})
            if rec_title_list is not None:
                title_list = title_list + rec_title_list
        return title_list
    else:
        return None
