'''
Created on May 23, 2018

@author: liuhou
'''

i = 0
l=[]
for i in range(20):
    if (len(l)==0):
        l.append(i)
    elif(len(l) == 1):
        l.append(int(l[0])+1)
    else:
        l.append(l[-1]+l[-2])
print(l)


def fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
 
print (fib(20))