from math import *
from turtle import *
f=open('27_1/27A.txt')
f.readline()
points=[list(map(float,s.replace(',','.').split())) for s in f]
# k=30
# penup()
# tracer(0)
# screensize(2000,2000)
# for x,y in points:
#     setpos(x*k,y*k)
#     dot()
# for x in range(-10,10):
#     for y in range(-10,10):
#         setpos(x*k,y*k)
#         if x==0 or y ==0:
#             dot(5,'red')
#         else:
#             dot()
# done()
clusters=[[],[]]
for x,y in points:
    if y > 1:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
# penup()
# k=30
# tracer(0)
# screensize(2000,2000)
# clrs=['pink','orange']
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,clrs[i])
# done()
best=[[],[]]
for i in range(len(clusters)):
    min_dist_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_dist_per_point=0
        for x1,y1 in clusters[i]:
            sum_dist_per_point+= dist([x,y],[x1,y1])
        if min_dist_per_cluster>sum_dist_per_point:min_dist_per_cluster=sum_dist_per_point;best[i]=[x,y]
P_X=sum([x for x,y in best])/len(best) #СРЕД АРИФМ
P_Y=sum([y for x,y in best])/len(best)
print(int(P_X*10000))
print(int(P_Y*10000))

