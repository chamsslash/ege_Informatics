import re

f=open('24_2.txt')
valid=re.findall(r'B\d+(?:[-*]\d+)*',f.read())
print(len(max(valid,key=len)))