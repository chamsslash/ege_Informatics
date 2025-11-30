from math import dist
f=open("27_B_2.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
k=3
clusters=[[]for _ in range(k)]
best=[[]for _ in range(k)]
#разбиваем на кластеры
for point in points:
    if point[1] < 4 and point[0]<3:
        clusters[0].append(point)
    elif point[0] > 5:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
for i in range(len(clusters)):
    min_sum_dist_cluster=float('inf')
    for x,y in clusters[i]:
        sum_dist_for_point=0
        for x1,y1 in clusters[i]:
            sum_dist_for_point += dist([x,y],[x1,y1])
        if min_sum_dist_cluster>sum_dist_for_point: min_sum_dist_cluster=sum_dist_for_point;best[i] = [x,y]
P_x =sum([x for x,y in best])/len(best)
P_y=sum([y for x,y in best])/len(best)
print(int(P_x*10000))
print(int(P_y*10000))