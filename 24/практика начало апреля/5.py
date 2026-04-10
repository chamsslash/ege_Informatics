import re
from re import*
f=open('24.5.txt')
data=f.readline()
valid=re.findall(r'[456][0456]*(?:[+*][456][0456]*)*',data)
print((max(valid,key=len)))
print(len(max(valid,key=len)))