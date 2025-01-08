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
    if len(sys.argv) != 2:
        exit()
    
    # Merr URL-në e dhënë si argument
    url = sys.argv[1]
    
    # Bën kërkesën për informacionet e përdoruesit nga GitHub API
    r = requests.get(url, DEFAULT_HEADERS)

    # Kontrollon statusin e përgjigjes dhe printon vendndodhjen e përdoruesit
    if r.status_code == 200:
        print(r.json()["location"])

    # Nëse përdoruesi nuk është gjetur (404)
    elif r.status_code == 404:
        print("Not found")

    # Nëse është tejkaluar kufiri i kërkesave (403)
    elif r.status_code == 403:
        rate_limit = int(r.headers["X-Ratelimit-Reset"])
        now = int(time.time())
        minutes = int((rate_limit - now) / 60)
        print("Reset in {} min".format(minutes))
