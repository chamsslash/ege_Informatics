from math import dist
from operator import indexOf
f = open('task27_4/27_B.txt')
f.readline()
k=3
points=[list[float](map(float,s.replace(",",".").split())) for s in f]
clusters=[[] for _ in range(k)]
best=[[] for _ in range(k)]
for x,y in points[:]:
    if x <0 or x>25:
        points.remove([x,y])
    elif y<15:
        clusters[0].append([x,y])
    elif y >21:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
for i in range(len(clusters)):
    min_sum_cluster=float('inf')
    for x,y in clusters[i]:
        sum_per_point=0
        for x1,y1 in clusters[i]:
            sum_per_point+=dist([x,y],[x1,y1])
        if min_sum_cluster>sum_per_point:min_sum_cluster=sum_per_point;best[i]=[x,y]
ts=[len(clust) for clust in clusters]
print(int(abs(best[ts.index(max(ts))][0]-best[ts.index(min(ts))][0])*10_000))
print(int(abs((best[ts.index(max(ts))][1]-best[ts.index(min(ts))][1])*10_000)))
