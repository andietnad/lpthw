#!/usr/bin/env python
from sys import argv

script, text = argv

def revert(text):
    string = ""
    for i in range(len(text)-1,-1,-1):
        string += text[i]
    return string

string = revert(text)
print(string)
