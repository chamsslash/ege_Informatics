from math import *
from turtle import *
f=open('27_1/27B.txt')
f.readline()
points=[list(map(float,s.replace(',','.').split())) for s in f]
# k=30
# penup()
# tracer(0)
# screensize(2000,2000)
# for x,y in points:
#     setpos(x*k,y*k)
#     dot(5,"blue")
# for x in range(-10,10):
#     for y in range(-10,10):
#         setpos(x*k,y*k)
#         if x ==0 or y ==0:
#             dot(5,'red')
#         else:
#             dot(5,'grey')
# done()  
k=3
clusters=[[] for _ in range(k)]  
best=[[] for _ in range(k)]  
for x,y in points:
    if y <0:
        clusters[0].append([x,y])
    elif x<2:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
for i in range(len(clusters)):
    min_dist_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_dist_per_cluster=0
        for x1,y1 in clusters[i]:
            sum_dist_per_cluster+= dist([x,y],[x1,y1])
        if min_dist_per_cluster>sum_dist_per_cluster:min_dist_per_cluster=sum_dist_per_cluster;best[i]=[x,y]
P_X=sum([x for x,y in best])/len(best) #СРЕД АРИФМ
P_Y=sum([y for x,y in best])/len(best)
print(int(P_X*10000))
print(int(P_Y*10000))

k=30
screensize(2000,2000)
tracer(0)
penup()
clrs=['midnight blue','deep pink','lime']
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,clrs[i])
done()