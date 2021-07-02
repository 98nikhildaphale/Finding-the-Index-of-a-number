# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:43:44 2021

"""


x=int(input())

y=[]

for i in range(x):
    temp=input()
    y.append(temp)


z=input()

if z in y:
   print("Yes the element is present")
a=y.index(z)
print("It is at position:",a)   
    