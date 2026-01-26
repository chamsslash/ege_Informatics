f = open("24.4.txt")
a = f.readline().strip()
from re import findall
op = findall(r"[345][0345]*(?:[-*][345][0345]*)*",a)
max=0
for o in op:
    eva=eval(o)
    if eva>max:
        max=eva
print(max)