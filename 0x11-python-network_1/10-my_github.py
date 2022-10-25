#!/usr/bin/python3
"""This takes the users GitHub username and password and uses the GibHub API to display their id
"""
if __name__ == "__main__":
    import sys
    import requests
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
