#!/usr/bin/env python3
"""
GitHub API:
Script that prints the location of a specific user
"""


import requests
import sys
import time


DEFAULT_HEADERS = {"Accept": "application/vnd.github.v3+json"}


if __name__ == "__main__":
    # Check if exactly one argument is passed (the URL)
    if len(sys.argv) != 2:
        exit()

    url = sys.argv[1]



    # Send a GET request to GitHub API for the user's information
    r = requests.get(url, headers=DEFAULT_HEADERS)

    # Check the response status code
    if r.status_code == 200:
        # If status is 200, print the user's location
        print(r.json().get("location", "No location found"))
    elif r.status_code == 404:
        # If status is 404, user not found
        print("Not found")

    elif r.status_code == 403:
        # If status is 403 (rate limit exceeded), print the time until reset
        rate_limit = int(r.headers["X-Ratelimit-Reset"])
        now = int(time.time())
        minutes = int((rate_limit - now) / 60)
        print("Reset in {} min".format(minutes))
