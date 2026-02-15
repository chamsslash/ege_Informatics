import math

f=open('Задание 5.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split()) )for i in f]
clusters=[]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points[:]:
            if math.dist(p,p1)<=1:
                points.remove(p1)
                clusters[-1].append(p1)
    if len(clusters[-1])<=10:
        del(clusters[-1])
print(len(clusters))
best=[[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p,p1)
        if msd<msdpc:
            msdpc=msd
            best[i]=p
res=[]
for i in range(len(clusters)):
    for j in range(i+1,len(clusters)):
        for u in clusters[i]:
            for v in clusters[j]:
                res.append(math.dist(u,v))
print(min(res),max(res))

