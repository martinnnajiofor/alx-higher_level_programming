#!/usr/bin/python3
"""This takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter and finally displays the body of the response
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], payload)
    print(r.text)
