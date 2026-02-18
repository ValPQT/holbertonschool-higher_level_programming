#!/usr/bin/python3
"""
API Data Retrieval and Storage Script.

This script fetches post data from the JSONPlaceholder API using the 'requests'
library, displays titles in the console, and saves a cleaned version
of the data into a CSV file.
"""

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from the API and print their titles to the console.

    Performs a GET request. If the response is successful (200),
    it iterates through the list of posts to print each 'title' field.
    """
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts, filter specific fields, and save them to a CSV file.

    Filters the API response to keep only 'id', 'title', and 'body'.
    The resulting data is written to 'posts.csv' using UTF-8 encoding.
    """
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

        cleaned_posts = []
        for post in posts:
            cleaned_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        # Added newline='' to prevent blank lines between rows in some OS
        with open('posts.csv', 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(cleaned_posts)

        print("Posts successfully saved to posts.csv")
    else:
        print("Failed to fetch data")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
