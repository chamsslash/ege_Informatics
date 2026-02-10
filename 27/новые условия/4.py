import math

f=open('27_4.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
while points:
    clusters.append([points[0]])
    del points[0]
    for p in clusters[-1]:
        for p1 in points[:]:
            # очень маленький 
            if math.dist(p1,p) < 0.1:
                points.remove(p1)
                clusters[-1].append(p1)
    if len(clusters[-1])<=10:
        del clusters[-1]
print(len(clusters))
bestie=[[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for a in clusters[i]:
        msd=0
        for b in clusters[i]:
            msd+=math.dist(a,b)
        if msd<msdpc:
            msdpc=msd
            bestie[i]=a
min_ix=clusters.index(min(clusters,key=len))
max_ix=clusters.index(max(clusters,key=len))
o1=bestie[min_ix][0]-bestie[max_ix][0]
o2=bestie[min_ix][1]-bestie[max_ix][1]
print(o1,o2)
