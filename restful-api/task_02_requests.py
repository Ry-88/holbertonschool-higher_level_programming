#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    status = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {status.status_code}")
    if status.status_code == 200:
        posts = status.json()
        for post in posts:
            print(post["tilte"])

def fetch_and_save_posts():
    status = requests.get('https://jsonplaceholder.typicode.com/posts')
    if status.status_code == 200:
        posts = status.json()
        
        posts_dec = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", "w", encoding="utf-8") as file:
            w = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            w.writeheader()
            w.writerow(posts_dec)
