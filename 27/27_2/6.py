from math import dist
f = open('task27_3/27B.txt')
f.readline()
k=3
points=[list[float](map(float,s.replace(",",".").split())) for s in f]
clusters=[[] for _ in range(k)]
best=[[] for _ in range(k)]
for x,y in points:
    if x>7.5 and x<11:
        clusters[0].append([x,y])
    elif y>5.9 and x<6:
        clusters[2].append([x,y])
    elif x<5.5 and x>1.5:
        clusters[1].append([x,y])
    else:
        continue
        #anomaly
for i in range(len(clusters)):
    min_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_per_point=0
        for x1,y1 in clusters[i]:
            sum_per_point+=dist([x,y],[x1,y1])
        if min_per_cluster>sum_per_point:
            min_per_cluster=sum_per_point;best[i]=[x,y]
p_x= sum([x for x,y in best])/len(clusters)
p_y= sum([y for x,y in best])/len(clusters)
print(p_x*10_000,p_y*10_000)