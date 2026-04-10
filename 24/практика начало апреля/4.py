import re
from re import*
f=open('24.4.txt')
data=f.readline()
valid=re.findall(r'[123][0123]*(?:[+*][123][0123]*)*',data)
print(max(valid,key=len))
print(len(max(valid,key=len)))

