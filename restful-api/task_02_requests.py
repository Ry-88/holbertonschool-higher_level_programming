#!/usr/bin/python3

import requests
import json


def fetch_and_print_posts():
    status = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print("Status Code:", status.status_code)
    if status.status_code == 200:
        status.json()
    print(status.headers['posts'])
