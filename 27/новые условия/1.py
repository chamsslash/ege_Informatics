# import math
#
# f=open('27_1.txt')
# f.readline()
# points=[list(map(float,i.replace(',','.').split())) for i in f]
# # начало кластеризации
# clusters=[]
# while points:
#     clusters.append([points[0]])
#     del (points[0])
#     for point in clusters[-1]:
#         for point1 in points[:]:
#             print(point,point1)
#             if math.dist(point,point1)<0.5:
#                 clusters[-1].append(point1)
#                 points.remove(point1)
#     if len(clusters[-1]) <= 10:
#         del (clusters[-1])
# # проверим кластеризацию
# from turtle import*
# penup()
# k=35
# screensize(2000,2000)
# tracer(False)
# clrs=['blue','red','green','yellow','orange','purple','cyan']
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,clrs[i])
#
# # находим центроидики
# bestie=[[]for _ in range(len(clusters))]
# for i in range(len(clusters)):
#     msdpc=float('inf')
#     for x,y in clusters[i]:
#         msd=0
#         for x1,y1 in clusters[i]:
#             msd+=math.dist([x,y],[x1,y1])
#         if msd<msdpc:
#             bestie[i]=[x,y]
#             msdpc=msd
# dist_centr_dot=list([math.dist(bestie[index],dotka) for index in range(len(clusters)) for dotka in clusters[1-index]])
# print(min(dist_centr_dot),max(dist_centr_dot))
# done()
import math

f=open('27_1.txt')
f.readline()
clusters=[]
p=[list(map(float,i.replace(",",".").split())) for i in f]
eps=1
while p:
    clusters.append([p[0]])
    del p[0]
    for p1 in clusters[-1]:
        for p2 in p:
            if math.dist(p1,p2) < eps:
                clusters[-1].append(p2)
                p.remove(p2)
    if len(clusters[-1])<=10:
        del clusters[-1]
best=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float("inf")
    for x,y in clusters[i]:
        msd=0
        for x1,y1 in clusters[i]:
            msd+=math.dist([x1,y1],[x,y])
        if msd<msdpc:
            msdpc=msd
            best[i]=[x,y]
P_x=sum([x for x,y in best])/len(best)
P_y=sum([y for x,y in best])/len(best)
P_s=sum(len(i)/(3*3) for i in clusters)
dist_centr_dot=[math.dist(best[index],dotka) for index in range(len(clusters)) for dotka in clusters[1-index]]
print(min(dist_centr_dot),max(dist_centr_dot))
from turtle import *
penup()
tracer(0)
colors=["red","green","blue","cyan"]
screensize(2000,2000)
k=85
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()