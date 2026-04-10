import re

f=open('24.3.txt', 'r')
data=f.readline()
# 0 кратны и 6 кратны
from re import*
valid=re.findall(r'(?:[123456789AB]+[\dAB])*[06]+',data)
print((max(valid,key=len)))
print(len(max(valid,key=len)))