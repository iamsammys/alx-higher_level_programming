#!/usr/bin/python3
"""
Created on Mon Aug 24 07:02:53 2020

"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
    print(response.text)
