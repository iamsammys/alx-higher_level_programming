#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "" or len(sentence) == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return (len(sentence), f_char)
