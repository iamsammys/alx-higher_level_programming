#!/bin/bash
# bash script that sends a JSON POST request to a URL passed as the first argument
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1"
