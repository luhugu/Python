#coding=utf-8
'''
Created on May 16, 2018

@author: liuhou
'''
from math import sqrt, ceil, floor

a = 1
while (a>0):
    a = a+1
    if (ceil(sqrt(a+100)) == floor(sqrt(a+100))) and (ceil(sqrt(a+268)) == floor(sqrt(a+268))):
        print(a)
        break
