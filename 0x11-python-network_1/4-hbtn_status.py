#!/usr/bin/python3
"""
   This uses the package requests to fetch https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
        response = requests.get('https://alx-intranet.hbtn.io/status')
        print("Body response:\n\t- type: {}\n\t- content: {}"
            .format(type(response.text), response.text))
