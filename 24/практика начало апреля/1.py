import re
import string
from string import printable
f=open('24.1.txt')
data=f.readline()
from re import*
valid=re.findall(r'[123456789ABCDEFGHIJ]+',data)
print(max(valid,key=len))
print(len(max(valid,key=len)))