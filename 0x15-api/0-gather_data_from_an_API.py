#!/usr/bin/python3
"""
0. Gather data from an API
"""
import requests
import sys


def get_user_info(usr_id):
    """
    Requests for all info related to user of id
    <usr_id>
    """
    url = "https://jsonplaceholder.typicode.com/users/{}"
    url = url.format(usr_id)
    response = requests.get(url)
    return response.json()


def get_todos(usr_id=None):
    """
    Returns a list of all todos
    If <usr_id> is not None filters todos
    for only those with provided use id
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if usr_id is None:
        return response.json()
    filteredlist = [x for x in response.json()
                    if str(x.get("userId", None)) == usr_id]
    return filteredlist


if __name__ == '__main__':
    if len(sys.argv) > 1:
        usr = get_user_info(sys.argv[1])
        if usr.get("name", None) is not None:
            usr_todos = get_todos(sys.argv[1])
            print("Employee {} is done with tasks({}/{}):".format(
                  usr.get("name"),
                  len([x for x in usr_todos if x.get("completed")]),
                  len(usr_todos)))
            for i in usr_todos:
                if i.get("completed") == False:
                    print("\t {}".format(i.get("title")))
