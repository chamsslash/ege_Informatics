import re

f=open('24.2.txt')
data=f.readline()
from re import*
valid=re.findall(r'(?:[123456789AB][0123456789AB]*)*[02468A]',data )
print(len(max(valid,key=len)))