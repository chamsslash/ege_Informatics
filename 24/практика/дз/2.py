f=open("дз/Задание 2.txt")
a=f.readline().strip()
from re import findall
op=findall(r'[123][0123]*(?:[+*][123][0123]*)*', a)
print(len(max(op,key=len)))
