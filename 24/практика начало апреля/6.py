import re

f=open('24.6.txt')
data=f.readline()
from re import*
validi=re.findall(r'[345][0345]*(?:[*][345][0345]*)*',data)
print(eval(max(validi,key=eval)))

