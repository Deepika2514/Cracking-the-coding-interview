# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:57:14 2020

@author: Deepika
"""
def StringComp(string):
    res = []
    i = j = 0
    while j < len(string):
        if string[i] != string[j]:
            res.append(string[i])
            res.append(str(j-i))
            i = j
        j += 1
        
    res.append(string[i])
    res.append(str(j-i))
    return "".join(res) if len(res) < len(string) else string

if __name__ == "__main__":
    string = "aabcccccaaa"
    print(StringComp(string))