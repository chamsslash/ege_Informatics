import re

f=open('24.9.txt')
data=f.readline()
from re import*
validi=re.findall(r'(?:0|[1-9][0-9]*)(?:[-*](?:0|[1-9][0-9]*))*',data)
print(max(validi,key=len))
print(len(max(validi,key=len)))