import math

f=open('27B.txt')
points=[list(map(float,point.replace(',','.').split())) for point in f]
eps=1
clusters=[]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points:
            if math.dist(p1,p) < eps:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        del(clusters[-1])
        print('anomaly')
print(clusters)
print(len(clusters))
# anti centroids
anties=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    maxspdc=0
    for p in clusters[i]:
        maxsd=0
        for p1 in clusters[i]:
            maxsd+= math.dist(p1,p)
        if maxsd>maxspdc:
            maxspdc=maxsd
            anties[i]=p
P_x=sum([x for x,y in anties])/len(anties)
P_y=sum([y for x,y in anties])/len(anties)
print(abs(P_x*10_000)//1, abs(P_y*10_000)//1)
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
