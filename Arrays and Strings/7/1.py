# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:03:23 2020

@author: Deepika
"""
def RotateMat(mat):
    N = len(mat)
    for i in range(N):
        for j in range(i+1, N):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(N):
        j = 0
        k = N-1
        while j < N//2:
            mat[i][j], mat[i][k] = mat[i][k], mat[i][j]
            j += 1
            k -= 1
    return mat
if __name__ == "__main__":
    mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(RotateMat(mat))