#!/bin/bash
# This script displays all methods the server will accept
curl -sI -L "$1" | grep "Allow" | cut -d ' ' -f 2-
