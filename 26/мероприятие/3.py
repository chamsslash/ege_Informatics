f=open("Задание 2.txt")
data=[]
f.readline()
zal_end=0
for i in f:
    start,end=map(int,i.split())
    data.append([end,start])
mers=[]
data.sort()
for end,start in data:
    if start>=zal_end:
        zal_end=end
        mers.append([start,end])
    if start>=1344:
        print(start,end)
mers.sort()
print(len(mers),mers)