#!/bin/bash
# This script sends a json POST request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
