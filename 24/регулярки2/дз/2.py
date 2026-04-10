d=open('Задание 2.txt')
data=d.readline().strip()
from re import *
valid=findall(r"D\d+(?:[-*]\d+)*",data)
t=max(valid,key=len)
print(t)
print(len(t))