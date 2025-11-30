# from math import dist

# f = open('task27_4/27_A.txt')
# f.readline()
# k=2
# clusters=[[] for _ in range(k)]
# best=[[] for _ in range(k)]
# points= [list(map(float,s.replace(',','.').split())) for s in f]
# for x,y in points:
#     if x>5.5:
#         clusters[0].append([x,y])
#     else:
#         clusters[1].append([x,y])
# for i in range(len(clusters)):
#     min_per_cluster=float('inf')
#     for x,y in clusters[i]:
#         sum_per_point=0
#         for x1,y1 in clusters[i]:
#             sum_per_point+=dist([x,y],[x1,y1])
#         if sum_per_point<min_per_cluster:
#             min_per_cluster=sum_per_point;best[i]=[x,y]
# P_x=max([x for x,y in best])
# P_y=max([y for x,y in best])
# print(int(P_x*10_000),int(P_y*10_000))
# 
# способ перебором  
from math import dist   
f = open('task27_4/27_A.txt')
f.readline()
k=2
best=[[] for _ in range(k)]
points= [list(map(float,s.replace(',','.').split())) for s in f]
min_sum_dist=float('inf')
for i in range(len(points)):
    for i1 in range(i+1,len(points)):
        t1,t2 = points[i],points[i1]
        sum_dist=0
        for t in points:
            sum_dist+=min(dist(t1,t),dist(t2,t))
        if min_sum_dist>sum_dist:
            min_sum_dist=sum_dist
            best=[t1,t2]
P_x=max([x for x,y in best])
P_y=max([y for x,y in best])
print(int(P_x*10_000),int(P_y*10_000))
