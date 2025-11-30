import dis
from inspect import ClosureVars
from math import *
from turtle import *
f=open('27_2/27B.txt')
f.readline()
points=[list(map(float,s.replace(',','.').split())) for s in f]
# k=30
# penup()
# screensize(2000,2000)
# tracer(0)
# for x,y in points:
#     setpos(x*k,y*k)
#     dot(5,'midnight blue')
# for x in range(-10,10):
#     for y in range(-10,10):
#         setpos(x*k,y*k)
#         if x==0 or y == 0 :
#             dot(5,'purple')
#         else:dot(5,'moccasin')
# done()
clrs=['midnight blue','deep pink','lime']
clusters=[[],[],[]]
best=[[],[],[]]
for x,y in points:
    if y>4:
        clusters[0].append([x,y])
    elif x<3 and y <1:clusters[1].append([x,y])
    else:clusters[2].append([x,y])
for i in range(len(clusters)):
    min_dist_per_cluster=float('inf')
    for p in clusters[i]:
        sum_dist_per_point=0
        for p1 in clusters[i]:
            sum_dist_per_point+=dist(p,p1)
        if min_dist_per_cluster>sum_dist_per_point:min_dist_per_cluster=sum_dist_per_point;best[i]=p
P_X=sum([x for x,y in best])/len(best) #СРЕД АРИФМ
P_Y=sum([y for x,y in best])/len(best)
print(int(P_X*10000))
print(int(P_Y*10000))   
k=30
penup()
tracer(0)
screensize(2000,2000)

for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,clrs[i])
done()