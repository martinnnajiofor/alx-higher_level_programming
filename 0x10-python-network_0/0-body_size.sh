#!/bin/bash
# This script displays the size of the body of a response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
