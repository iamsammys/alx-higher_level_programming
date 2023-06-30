#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL
curl -Is $1 | grep Allow | cut -c 8-
