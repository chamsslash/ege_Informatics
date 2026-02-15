import math

f=open('Задание 1.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split() ))for i in f]
clusters=[]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points[:]:
            if math.dist(p1,p)<=5:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<=10:
        print('ANOMALY')
        del clusters[-1]
print(len(clusters))
best=[[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for a in clusters[i]:
        msd=0
        for b in clusters[i]:
            msd+=math.dist(a,b)
        if msd<msdpc:
            msdpc=msd
            best[i]=a
res=[math.dist(best[i],dot)for i in range(len(clusters)) for dot in clusters[1-i]]
print(max(res),min(res))
# что-то хуйня да нарисовать бара уже
from turtle import *
colors=['red','green','blue','cyan','purple','yellow']
k=50
tracer(0)
screensize(2000,2000)
penup()

for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])

done()