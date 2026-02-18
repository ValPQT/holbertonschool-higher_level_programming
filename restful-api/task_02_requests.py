#!/usr/bin/python3

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(url)
    print(f"Status Code : {response.status_code}")
    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        cleaned_posts = []
        for post in data:
            cleaned_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open('data.csv', 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(cleaned_posts)

        print("Posts successfully saved to data.csv")
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
