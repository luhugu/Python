'''
Created on May 23, 2018

@author: liuhou
'''
import time
import calendar
print (time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time())))

time.sleep(2)
 
print (time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time())))

cal = calendar.month(2018,5)
print(cal)