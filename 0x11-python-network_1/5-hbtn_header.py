#!/usr/bin/python3
"""This takes in a URL, sends a rquest to the URL and displays the value of the variable
X-Request-Id it the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get(sys.argv[1])
    html = req.headers
    print(html.get('X-Request-Id'))
