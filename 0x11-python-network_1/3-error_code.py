#!/usr/bin/python3
"""
   This is a Python script that takes in a URL, 
   sends a request to the URL 
   and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as reponse:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')

