#coding=utf-8

'''
Created on 2018年5月14日

@author: luhug
'''

from pip._vendor.distlib.compat import raw_input

profit = int(raw_input('Profit:'))
scope = [1000000, 600000, 400000, 200000, 100000,0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for i in range(0,6):
    if (profit>scope[i]):
        r += (profit-scope[i])*rate[i]
        profit = scope[i]
print(r)