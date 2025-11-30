from math import dist
f = open('task27_2/27A.txt')
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
k=2
clusters=[[] for _ in range((k))]
best=[[] for _ in range((k))]
for x,y in points:
    if y<0:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
for i in range(len(clusters)):
    min_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_for_point=0
        for x1,y1 in clusters[i]:
            sum_for_point+=  dist([x,y],[x1,y1])
        if min_per_cluster>sum_for_point:
            min_per_cluster=sum_for_point;best[i]=[x,y]
print(sum([x for x,y in best])/len(best)*10_000)
print(sum([y for x,y in best])/len(best)*10_000)