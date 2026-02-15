import math

f=open('27_7.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split()))for i in f]
clusters=[]
while points:
    clusters.append([points[0]])
    del points[0]
    for p in clusters[-1]:
        for p1 in points:
            if math.dist(p1,p) < 1:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        print('anomaly')
        del clusters[-1]
print(len(clusters))
best=[[]for _ in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p1,p)
        if msd<msdpc:
            msdpc=msd
            best[i]=p
disti=[]
for i in range(len(clusters)):
    for i1 in range(i+1,len(clusters)):
        for u1 in clusters[i]:
            for u2 in clusters[i1]:
                disti.append(math.dist(u1,u2))
print(min(disti),max(disti))
