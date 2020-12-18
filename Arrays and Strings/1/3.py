# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:48:47 2020

@author: Deepika
"""

def isUnique(string):
    checker = 0
    for elem in string:
        val = ord(elem) - ord("a")
        if (checker & (1 << val)) > 0:
            return False
        checker = (checker | (1 << val))
    return True

if __name__ == "__main__":
    string = "abcdefd"
    print(isUnique(string))