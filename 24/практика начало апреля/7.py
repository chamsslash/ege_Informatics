import re

f=open('24.7.txt')
data=f.readline()
from re import *
validi=re.findall(r'[789][0789]*(?:[*][789][0789]*)*',data)
print(max(validi,key=eval))
print(eval(max(validi,key=eval)))