f=open('Задание 1.txt')
data=f.readline().strip()
from  re import*
validi=findall(r'B\d+(?:[+]\d+)*',data)
poschet=[int(eval(i[1:])) for i in validi]
poschet.sort(reverse=True)
print(poschet[:5])