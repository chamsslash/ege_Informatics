f=open("дз/Задание 3.txt")
a=f.readline().strip()
from re import findall
op=findall(r'[234][0234]*(?:[+*][234][0234]*)*', a)
print(len(max(op,key=len)))
