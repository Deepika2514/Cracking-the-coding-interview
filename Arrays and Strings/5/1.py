# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:01:55 2020

@author: Deepika
"""

def OneAway(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    ptr1 = 0
    ptr2 = 0
    diff = 0
    if abs(n1 - n2) > 1:
        return False
    
    if n1 == n2:
        while ptr1 < n1 and ptr2 < n2:
            if string1[ptr1] != string2[ptr2]:
                diff += 1
                if diff > 1:
                    return False
            ptr1 += 1
            ptr2 += 1
    elif n1 > n2:
         while ptr1 < n1 and ptr2 < n2:
             if string1[ptr1] != string2[ptr2]:
                diff += 1
                if diff > 1:
                    return False
             else:
                ptr2 += 1
             ptr1 += 1
    else:
        while ptr1 < n1 and ptr2 < n2:
             if string1[ptr1] != string2[ptr2]:
                diff += 1
                if diff > 1:
                    return False
             else:
                ptr1 += 1
             ptr2 += 1
        
    return ptr1 == n1 or ptr2 == n2
        
    

if __name__ == "__main__":
    string1 = "palessb"
    string2 = "baless"
    print(OneAway(string1, string2))