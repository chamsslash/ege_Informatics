f=open("дз/Задание 5.txt")
a=f.readline().strip()
res=[]
b=[]
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    a=a.replace(i," ")
    b=a.split()
for ba in b:
    if all(int(digit) % 2 != 0 for digit in ba):
        res.append(int(ba))
print(max(res))
