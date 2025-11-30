from math import dist
f= open("27B_1.txt")
f.readline()
points=[(list(map(float,s.replace(",",".").split())))for s in f]
k=3
clusters=[[] for _ in range(k)]
for x,y in points:
    if y>10:
        clusters[0].append([x,y])
    elif x<2:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
best_cents=[[] for _ in range(k)]
for i in range(len(clusters)):
    min_sum_dist=float("inf")
    for x1,y1 in clusters[i]:
        sum_dist_per_point=0
        for x2,y2 in clusters[i]:
            sum_dist_per_point+= dist([x1,y1],[x2,y2])
        if min_sum_dist>sum_dist_per_point:min_sum_dist=sum_dist_per_point;best_cents[i]=[x1,y1]
P_X=sum([x for x,y in best_cents])/len(best_cents)
P_Y=sum([y for x,y in best_cents])/len(best_cents)
print(int(P_X*10000))
print(int(P_Y*10000))