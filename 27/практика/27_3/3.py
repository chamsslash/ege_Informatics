import math
from turtle import *
f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
eps=0.5
colors=['red','blue','cyan','purple','orange','pink']

clusters=[]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p in clusters[-1]:
        for p1 in points:
            if math.dist(p1,p) < eps:
                clusters[-1].append(p1)
                points.remove(p1)
    if len(clusters[-1])<10:
        print('Anomal')
        del clusters[-1]
print(len(clusters))
dists=[]
for n in range(len(clusters)):
    for n1 in range(n+1,len(clusters[n])):
        if n1<=(len(clusters)-1):
            for p in clusters[n]:
                for p1 in clusters[n1]:
                    dists.append(math.dist(p,p1))
print(min(dists)*10_000,max(dists)*10_000)
# # checkup
# penup()
# tracer(0)
# k=35
# screensize(2000,2000)
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,colors[i])
#
#
# done()
