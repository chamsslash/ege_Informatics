import math
from turtle import *
f=open("27A.txt")
f.readline()
points=[list(map(float,i.replace(",",".").split())) for i in f]
clusters=[]
eps=0.25
while points:
    clusters.append([points[0]])
    del points[0]
    for point in clusters[-1]:
        for point1 in points[:]:
            if math.dist(point,point1)<eps:
                clusters[-1].append(point1)
                points.remove(point1)
# colors=["red","yellow","blue"]
# tracer(0)
# k=30
# screensize(2000,2000)
# penup()
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,colors[i])
# penup()
# for x in range(-10,10):
#     for y in range(-10,10):
#         setpos(x*k,y*k)
#         dot(5)
# done()
# алгоритм централизации кластеров
best_centroid=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist=float("inf")
    for x,y in clusters[i]:
        sum_dist=0
        for x1,y1 in clusters[i]:
            sum_dist+=math.dist([x,y],[x1,y1])

        if sum_dist<min_sum_dist:
            min_sum_dist=sum_dist
            best_centroid[i]=[x,y]
print(best_centroid)
D_x=sum(x for x,y in best_centroid)/ len(best_centroid)
D_y=sum(y for x,y in best_centroid)/ len(best_centroid)
plotnost=0
for i in clusters:
    plotnost+=len(i)/(4*4)
print(abs(D_x+D_y)*10_000,int(abs(plotnost*10_000)))
