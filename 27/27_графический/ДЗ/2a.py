from math import dist
f=open("27_A_2.txt")
f.readline()
points= [list(map(float,s.replace(",",'.').split())) for s in f]
k=2
clusters=[[] for _ in range(k)]
best=[[] for _ in range(k)]
for x,y in points:
    if y<3:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
for i in range(len(clusters)):
    min_sum_dist=float('inf')
    for x,y in clusters[i]:
        sum_dist=0
        for x1,y1 in clusters[i]:
            sum_dist+=dist([x,y],[x1,y1])
        if min_sum_dist>sum_dist: min_sum_dist=sum_dist;best[i]=[x,y]
P_X=sum([x for x,y in best])/len(best)
P_Y=sum([y for x,y in best])/len(best)
print(int(P_X*10000))
print(int(P_Y*10000))