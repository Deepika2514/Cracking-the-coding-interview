# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:55:12 2020

@author: Deepika
"""
def StringRot(string1, string2):
    string1 += string1
    if string2 in string1:
        return True
    return False

if __name__ == "__main__":
    string2 = "waterbottld"
    string1 = "erbottlewat"
    print(StringRot(string1, string2))