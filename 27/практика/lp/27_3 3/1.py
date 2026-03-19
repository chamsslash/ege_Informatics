import math

f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
eps=0.5
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points:
            if math.dist(p1,p) < eps:
                clusters[-1].append(p1)
                points.remove(p1)
    if len (clusters[-1])<=10:
        print('Anomaly')
        del(clusters[-1])
besties=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p1,p)
        if msd<msdpc:
            msdpc=msd
            besties[i]=p
print(besties)
P_x=sum([i[0]for i in besties])/len(besties)
P_y=sum([i[1]for i in besties])/len(besties)

print(P_x*10_000,P_y*10_000)
from  turtle import *
tracer(0)
penup()
screensize(2000,2000)
k=35
clrs=['red','blue','pink','cyan','orange','purple','black','green']
for i in range(len(clusters)):
        for x,y in clusters[i]:
            setpos(x*k,y*k)
            dot(5,clrs[i])

done()