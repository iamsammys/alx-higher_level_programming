#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL
curl -Is | grep Allowed | cut -c 8-
