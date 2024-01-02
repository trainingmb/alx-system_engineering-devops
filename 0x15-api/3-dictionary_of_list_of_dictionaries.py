#!/usr/bin/python3
"""
3. Dictionary of list of dictionaries
"""
import json
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


def get_users():
    """
    Requests all info for all users
    """
    url = "https://jsonplaceholder.typicode.com/users"
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


def export_to_json(data, filename):
    """
    Write <data> to <filename>.json
    """
    filename = str(filename)
    with open(filename + ".json", 'w', encoding='UTF8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    all_users = get_users()
    usernames = {}
    data = {}
    for usr in all_users:
        usernames[usr.get("id")] = usr.get("username")
        data[usr.get("id")] = []
    all_todos = get_todos()
    for todo in all_todos:
        row = {}
        row["username"] = usernames[todo.get("userId")]
        row["task"] = todo.get("title")
        row["completed"] = todo.get("completed")
        data[todo.get("userId")].append(row)
    export_to_json(data, "todo_all_employees")
