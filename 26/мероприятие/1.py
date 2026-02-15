f=open('26.3 (1).txt')
zal_end=0
f.readline()
data=[]
for u in f:
    start,end=map(int,u.split())
    data.append([end,start])
data.sort()
mers=[]
for end,start in data:
    if start>zal_end:
        zal_end=end
        mers.append([end,start])
    if start>=1379:
        print(start,end)
    else:
        continue
mers.sort()
res=[ end for end,start in data if start>=1379]
print(len(mers),max(res),res)