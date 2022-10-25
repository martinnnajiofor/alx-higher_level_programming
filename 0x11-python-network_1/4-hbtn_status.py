#!/usr/bin/python3
"""
   This uses the package requests to fetch https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
        resp = requests.get('https://alx-intranet.hbtn.io/status')
        print("Body response:\n\t- type: {}\n\t- content: {}"
            .format(type(resp.text), resp.text))
