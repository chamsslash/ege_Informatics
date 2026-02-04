import math

f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
epsilon=0.25
while points:
    clusters.append([points[0]])
    del points[0]
    for i in clusters[-1]:
        for j in points[:]:
            if math.dist(i,j)<=epsilon:
                clusters[-1].append(j)
                points.remove(j)
    if len(clusters[-1])<=10:
        del clusters[-1]
best=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msd=float('inf')
    for x,y in clusters[i]:
        min_dist=0
        for x1,y1 in clusters[i]:
            min_dist+=math.dist([x,y],[x1,y1])
        if min_dist<msd:
            msd=min_dist
            best[i]=[x,y]
P_x=sum(x[0] for x in best)/len(best)*10_000
P_y=sum(x[1] for x in best)/len(best)*10_000
print(P_x,P_y)

colors=["blue","red","green","cyan"]
from turtle import *
penup()
screensize(2000,2000)
tracer(0)
k=45
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()