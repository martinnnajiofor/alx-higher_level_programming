#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL
curl $1 -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
