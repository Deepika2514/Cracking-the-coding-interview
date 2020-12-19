# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:24:50 2020

@author: Deepika
"""

def Zeromat(mat):
    res = set()
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                res.add((i,j))
    for elem in res:
        i, j = elem[0], elem[1]
        for k in range(N):
            mat[i][k] = 0
        for k in range(M):
            mat[k][j] = 0
    return mat

if __name__ == "__main__":
    mat = [[1,2,3,4],[5,0,7,8],[6,1,1,2],[2,3,4,0]]
    print(Zeromat(mat))