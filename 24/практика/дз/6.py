f=open("дз/Задание 6.txt")
a=f.readline().strip()
res=[]
from re import findall
op=findall(r'(?:0|[123456789][\d]*)(?:[+*](?:0|[123456789][\d]*))*',a)
# r'(?:0|[1-9][0-9]*)(?:[+*](?:0|[1-9][0-9]*))*'
for i in op:
    if eval(i)==0:
        res.append(i)
print(len(max(res,key=len)))