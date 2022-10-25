#!/usr/bin/python3
"""This takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter and finally displays the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    parameter = {'email': argv[2]}
    body = requests.post(argv[1], parameter)
    print(body.text)
