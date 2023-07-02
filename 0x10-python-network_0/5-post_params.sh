#!/bin/bash
# bash script that takes in a URL, sends a POST request to the passed URL
curl -sd "subject=I will always be here for PLD&&email=test@gmail.com" $1
