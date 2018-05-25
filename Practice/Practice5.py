'''
Created on May 23, 2018

@author: liuhou
'''
from click._compat import raw_input
l=[]
for i in range(3):
    x = int(raw_input("Input Integer:"))
    l.append(x)

l.sort(reverse=True)
print(l)