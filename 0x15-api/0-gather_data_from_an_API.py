#!/usr/bin/python3
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
    if usr_id == None:
        return response.json()
    print(response.json())
    filteredlist = [x for x in response.json()
                    if str(x.get("userId", Non)e) == usr_id]
    return filteredlist

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv[1])
        print(get_user_info(sys.argv[1]))
        print(get_todos(sys.argv[1]))
