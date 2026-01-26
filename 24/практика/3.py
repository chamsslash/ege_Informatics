f = open("24.3.txt")
a = f.readline().strip()
from re import findall
op = findall(r"[456][0456]*(?:[+*][456][0456]*)*",a)
print(len(max(op, key=len)))