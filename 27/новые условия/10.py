import math

f=open('Задание 4.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]

while points:

    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points[:]:
            if math.dist(p,p1)<=1:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        del clusters[-1]
print(len(clusters))
best=[[]for _ in range(len(clusters))]

for i in range (len(clusters)):
    msdpc=float('inf')
    for a in clusters[i]:
        msd=0
        for b in clusters[i]:
            msd+=math.dist(a,b)
        if msd<msdpc:
            msdpc=msd
            best[i]=a
min_ix,max_ix=clusters.index(min(clusters,key=len)),clusters.index(max(clusters,key=len))
res1=sum([math.dist(best[min_ix],point )for point in clusters[min_ix]])/(len(clusters[min_ix])-1)
res2=sum([math.dist(best[max_ix],point )for point in clusters[max_ix]])/(len(clusters[max_ix])-1)
print(res1,res2)