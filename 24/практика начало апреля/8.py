import re

f=open('24.8.txt')
data=f.readline()
from re import*
validi=re.findall(r'(?:o|[+-]?[1234][01234]*)(?:[+-](?:o|[1234][01234]*))*',data)
print(len(max(validi,key=len)))