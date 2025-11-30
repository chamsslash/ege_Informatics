from math import dist

#По условию надо не дистовое растояние
f=open('task27_2/27B.txt')
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
k=3
best=[[] for _ in range(k)]
clusters=[[] for _ in range(k)]
for x,y in points:

    if x<0:
        clusters[0].append([x,y])
    elif y<0:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
for i in range(len(clusters)):
    min_per_clust=float('inf')
    for x,y in clusters[i]:
        sum_per_point=0
        for x1,y1 in clusters[i]:
            # sum_per_point+= dist([x,y],[x1,y1])
            sum_per_point+=abs(x1-x)+abs(y1-y)
        if min_per_clust>sum_per_point:min_per_clust=sum_per_point;best[i]=[x,y]
print(abs(sum([x for x,y in best])/len(best)*10_000))
print(abs(sum([y for x,y in best])/len(best)*10_000))