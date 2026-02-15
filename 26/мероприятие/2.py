f=open("Задание 1.txt")
f.readline()
data=[]
for i in f:
    start,end = map(int,i.split())
    data.append([end,start])
data.sort()
zal_end=0
res=[]
for end,start in data:
    if start>=zal_end:
        zal_end=end
        res.append([start,end])
    if start>=1344:
        print(start,end)
res.sort()
print(len(res),res)