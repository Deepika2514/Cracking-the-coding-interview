# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:15:19 2020

@author: Deepika
"""



def checkPerm(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(string1) and ptr2 < len(string2):
        if string1[ptr1] != string2[ptr2]:
            return False
        ptr1 += 1
        ptr2 += 1
    return False if (ptr1 < len(string1) or ptr2 < len(string2)) else True

if __name__ == "__main__":
    string1 = "abc"
    string2 = "abd"
    print(checkPerm(string1, string2))