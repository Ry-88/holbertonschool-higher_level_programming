#!/usr/bin/python3

import requests


def fetch_and_print_posts():
    status = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", status.status_code)
    if status.status_code == 200:
        posts = status.json()
        for post in posts:
            print(post["tilte"])
