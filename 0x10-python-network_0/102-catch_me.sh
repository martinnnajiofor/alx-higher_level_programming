#!/bin/bash

curl -sL -X PUT 0.0.0.0:5000/catch_me -d user_id=98 -H "Origin: You got me!"
