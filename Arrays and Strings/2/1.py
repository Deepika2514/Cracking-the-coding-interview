# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:12:27 2020

@author: Deepika
"""

import collections

def checkPerm(string1, string2):
    hm1 = collections.Counter(string1)
    hm2 = collections.Counter(string2)
    if hm1 == hm2:
        return True
    else:
        return False

if __name__ == "__main__":
    string1 = "abc"
    string2 = "abc"
    print(checkPerm(string1, string2))