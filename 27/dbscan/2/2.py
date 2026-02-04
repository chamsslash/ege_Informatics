import math
from turtle import *
f=open("27B.txt")
f.readline()
points=[list(map(float,point.replace(",",".").split())) for point in f ]
# кластеризуем
clusters=[]
epsilon=0.25
while points:
    clusters.append([points[0]])
    del points[0]
    for point in clusters[-1]:
        for point1 in points[:]:
            if math.dist(point,point1) < epsilon:
                clusters[-1].append(point1)
                points.remove(point1)
    if len(clusters[-1])<=10:
        del clusters[-1]

# tracer(0)
# screensize(2000,2000)
# k=45
# penup()
# colors=["red","green","blue","yellow","pink","orange","cyan","violet","peach"]
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(colors[i])
#
# done()
best_centroid=[[] for point in clusters]
for i in range(len(clusters)):
    msdpc=float("inf")
    for point in clusters[i]:
        msd=0
        for point1 in clusters[i]:
            msd+=math.dist(point,point1)
        if msd<msdpc:
            msdpc=msd
            best_centroid[i]=point
P_x=sum(x[0] for x in best_centroid)/len(best_centroid)
P_y=sum(x[1] for x in best_centroid)/len(best_centroid)
P_s=sum(len(cluster)/(4*4) for cluster in clusters)
print(abs(P_x+P_y)*10_000,abs(P_s)*10_000)
