#!/bin/bash
# bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
url=$1
curl -Is url | grep Content-Length | cut -f2 -d " "
