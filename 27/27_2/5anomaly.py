from math import dist


f = open('task27_3/27A.txt')
f.readline()
k=2
points=[list(map(float,s.replace(",",".").split())) for s in f]
clusters=[[] for _ in range(k)]
for x,y in points:
    if x>5:
        clusters[0].append([x,y])
    elif y<5:
        clusters[1].append([x,y])
    else:
        #аномалии
        print(x,y)
best=[[] for _ in range(k)]
for i in range(len(clusters)):
    min_clust=float('inf')
    for x,y in clusters[i]:
        sum_per_point=0
        for x1,y1 in clusters[i]:
            sum_per_point+=dist([x,y],[x1,y1])
        if min_clust>sum_per_point:
            min_clust=sum_per_point;best[i]=[x,y]
p_x= sum([x for x,y in best])/len(clusters)
p_y= sum([y for x,y in best])/len(clusters)
print(p_x*10_000,p_y*10_000)