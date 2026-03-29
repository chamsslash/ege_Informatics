import re

f=open('24_1.txt')
data=f.readline().strip()
from re import*

validi=re.findall(r'A\d+(?:[+]\d+)*',data)
print(max(eval(i[1:])for i in validi))