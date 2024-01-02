#!/usr/bin/python3
"""
1. Export to CSV
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


def export_to_csv(data, filename):
    """
    Write <data> to <filename>.csv
    """
    filename = str(filename)
    with open(filename + ".csv", 'w', encoding='UTF8') as f:
        for row in data:
            f.write('"{}","{}","{}","{}"\n'.format(
                    row[0], row[1], row[2], row[3]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        usr = get_user_info(sys.argv[1])
        if usr.get("name", None) is not None:
            usr_todos = get_todos(sys.argv[1])
            data = []
            for i in usr_todos:
                row = [usr.get("id"),
                       usr.get("name"),
                       str(i.get("completed")),
                       i.get("title")]
                data.append(row)
            export_to_csv(data, usr.get("id"))
