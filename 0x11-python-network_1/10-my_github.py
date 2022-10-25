#!/usr/bin/python3
""" This script takes the users GitHub
username and password and uses the GitHub API to display their id"""
import requests
from sys import argv

if __name__ == '__main__':
    url = f"https://api.github.com/user"
    res = requests.get(url, auth=(argv[1], argv[2]))
    get_id = res.json()
    print(get_id.get('id'))
