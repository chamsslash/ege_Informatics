import math

f=open('Задание 2.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split()) )for i in f]
clusters=[]
best=[[]for _ in range(len(points))]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points:
            if math.dist(p,p1)<=1:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        del(clusters[-1])
print(len(clusters))
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p,p1)
        if msd<msdpc:
            msdpc=msd
            best[i]=p
bests_dist=math.dist(best[0],best[1])
res=[math.dist(popa,best[i])for i in range(len(clusters)) for popa in clusters[i]]
print(bests_dist,max(res))
