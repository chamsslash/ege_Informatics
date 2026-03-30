import math

f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
# clusterization
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
    if len(clusters[-1])<=10:
        print('Anomaly')
        del(clusters[-1])

print(clusters)
print(len(clusters))
dists=[]
for n in range(len(clusters)):
    for n1 in range(n+1,len(clusters)):
        if n1<=(len(clusters)-1):
            for p in clusters[n]:
                for p1 in clusters[n1]:
                    dists.append(math.dist(p,p1))

print(min(dists)*10_000)
print(max(dists)*10_000)
        #  visual
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