import math

f=open('27B.txt')
f.readline()
clusters=[]
points=[list(map(float,i.replace(',','.').split()))for i in f]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points[:]:
            if math.dist(p1,p) <= 0.5:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        print('Anomaly')
        del(clusters[-1])
bestie=[[] for i in range(len(clusters))]
for ii in range(len(clusters)):
    msdpc=float('inf')
    for o in clusters[ii]:
        msd=0
        for o1 in clusters[ii]:
            msd+=math.dist(o[:2],o1[:2])
        if msd<msdpc:
            msdpc=msd
            bestie[ii]=o
print(bestie)
starshine=[]
for yk in range(len(clusters)):
    brs=sum([brbr for x,y,brbr in clusters[yk]])/len(clusters[yk])
    starshine.append(brs)
print(sum([x+y for x,y,brbr in bestie])*10_000)
print(sum(starshine)*10_00)