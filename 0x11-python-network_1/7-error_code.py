#!/usr/bin/python3
"""This takes in a URL, sends a request to the URL and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import requests
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
