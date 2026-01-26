f = open("дз/Здаание 4.txt")
a = f.readline().strip()
from re import findall

op = findall(r"[345][0345]*(?:[*][345][0345]*)*", a)
print(eval(max(op, key=eval)))
