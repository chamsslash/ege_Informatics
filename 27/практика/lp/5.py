import math

f=open('Задание 5B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
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
        print('Anomaly')
        del(clusters[-1])

besties=[[]for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+=math.dist(p1,p)
        if msd<msdpc:
            msdpc=msd
            besties[i]=p
print(len(clusters))
# p1=min([math.dist(i,[-2.2,0]) for i in besties])
# p2=max([math.dist(i,[0,-2.0]) for i in besties])
# print(p1,p2)
maxi=besties.index(max(besties,key=len))
mini=besties.index(min(besties,key=len))
o1=[1 for i in clusters[maxi] if  0.5 <= math.dist(i,besties[maxi]) <= 2.5]
o2=[1 for i in clusters[mini] if  0.4 <= math.dist(i,besties[mini]) <= 1.6]
print(sum(o1))
print(sum(o2))
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