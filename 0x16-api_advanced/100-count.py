#!/usr/bin/python3
"""
3. Count it!
"""
import requests
import re


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
            title_list.append(child.get('data', {}).get('title').lower())
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


def count_words(subreddit, word_list):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript, but
    java should not).
    """
    title_list = recurse(subreddit)
    if title_list is None:
        return None
    search_pattern = r'(?:(?<=^)|(?<=\s))({})(?=\s|$)'
    word_list = [i.lower()  for i in word_list]
    searches = [search_pattern.format(i)  for i in word_list]
    results = {}
    for i in word_list:
        results[i] = 0
    for title in title_list:
        for i in range(len(searches)):
            o = re.findall(searches[i], title)
            results[word_list[i]] += len(o)
    results_sorted = sorted(results.items(),
                            key=lambda x: x[1],
                            reverse=True) 
    for key, value in results_sorted:
        print("{}: {}".format(key, value))
    return (title_list, results)
