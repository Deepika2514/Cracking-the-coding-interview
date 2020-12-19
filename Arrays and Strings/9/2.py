# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:02:53 2020

@author: Deepika
"""

def StringRot(string1, string2):
    i = 0
    j = 0
    start = -1
    while i < len(string2):
        if string1[j] == string2[i]:
            start = i
            break
        else:
            i += 1
#    print(start)
#    print(string2[start:len(string2)] + string2[0:start])
    if string1 == string2[start:len(string2)] + string2[0:start]:
        return True
    else:
        return False

if __name__ == "__main__":
    string2 = "erbottlewat"
    string1 = "erbottlewat"
    print(StringRot(string1, string2))