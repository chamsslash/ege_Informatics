import math

f=open('27_6.txt')
f.readline()
points=[ list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
while points:
    clusters.append([points[0]])
    del points[0]
    for p in clusters[-1] :
        for p1 in points[:]:
            if math.dist(p,p1) <= 1:
                points.remove(p1)
                clusters[-1].append(p1)
    if len(clusters[-1])<=10:
        del clusters[-1]
print(len(clusters))
print([len(clusters[i]) for i in range(len(clusters))])
best=[[]for _ in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p,p1)
        if msd<msdpc:
            msdpc=msd
            best[i]=p
min_i,max_i =clusters.index(min(clusters,key=len)),clusters.index(max(clusters,key=len))
print(min_i,max_i)
o=sum([math.dist(point,best[min_i])for point in clusters[min_i]])/(len(clusters[min_i])-1)
o1=sum([math.dist(point,best[max_i])for point in clusters[max_i]])/(len(clusters[max_i])-1)
print(o,o1)
