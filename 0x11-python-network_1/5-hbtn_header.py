#!/usr/bin/python3
"""
Created on Mon Aug 24 07:02:53 2020

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
