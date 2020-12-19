# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:51:25 2020

@author: Deepika
"""
def setNone(mat,row, col):
    for i in range(len(mat)):
        mat[i][col] = None
    for i in range(len(mat[0])):
        mat[row][i] = None
    return mat

def Zeromat(mat):
    M = len(mat)
    N = len(mat[0])
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                mat = setNone(mat,i,j)
    for i in range(M):
        for j in range(N):
            if mat[i][j] == None:
                mat[i][j] = 0
    return mat

if __name__ == "__main__":
    mat = [[1,2,3,4],[5,0,7,8],[6,1,1,2],[2,3,4,0]]
    print(Zeromat(mat))