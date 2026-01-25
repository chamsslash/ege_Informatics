f=open("дз/Задание 4.txt")
a=f.readline().strip()
b=[]
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    a=a.replace(i," ")
    b=a.split()
res=[]
for ba in b:
    if len(ba)==6 and ba[0] != '0':
        res.append(int(ba))
print(min(res))