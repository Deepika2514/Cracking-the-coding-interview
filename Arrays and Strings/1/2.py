# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:45:23 2020

@author: Deepika
"""



def isUnique(string):
    string = sorted(string)
    for i in range(len(string)-1):
        if i != 0 and string[i] == string[i-1]:
            return False
    return True
            

if __name__ == "__main__":
    string = "abcdefd"
    print(isUnique(string))