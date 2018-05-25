#coding=utf-8
'''
Created on May 16, 2018

@author: liuhou
'''
from click._compat import raw_input
d = raw_input("Please enter date, Format is YYYYMMDD:")
dStr = str(d)
year = int(dStr[0:4])
month = int(dStr[4:6])
day = int(dStr[6:8])
ml = [1,2,3,4,5,6,7,8,9,10,11,12]
dl = [31,28,31,30,31,30,31,31,30,31,30,31]

dayCount = 0
leap = 0
for m in range(0,12):
    if (ml[m]<month):
        dayCount += dl[m]

dayCount += day

if (year%400 == 0) or (year%100 != 0 and year%4 == 0):
    leap = 1
    
if (month>2):
    dayCount += leap
    
print(dayCount)
