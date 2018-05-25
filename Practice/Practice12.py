# coding=utf-8

'''
Created on May 24, 2018
找出100到200之间的素数
@author: liuhou
'''
l=[]
flag = 0
from math import sqrt
for i in range(101,200):
    x = int(sqrt(i+1))
    for j in range(2, x+1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        l.append(i)
    flag = 0

print(l)