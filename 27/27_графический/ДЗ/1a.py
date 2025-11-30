from math import dist
f=open("27_A_1.txt")
f.readline()
points=[(list(map(float,s.replace(",",".").split()))) for s in f]
clusters=[[],[]]
for x,y in points:
    if x>16:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
best_centroids=[[],[]]
for i in range(len(clusters)):
    min_sum_dist=float('inf')
    for x1,y1 in clusters[i]:
        sum_dist_per_first_point=0
        for x2,y2 in clusters[i]:
            sum_dist_per_first_point+=dist([x1,y1],[x2,y2])
        if sum_dist_per_first_point<min_sum_dist:
            min_sum_dist = sum_dist_per_first_point
            best_centroids[i] = [x1, y1]
print(best_centroids)
p_x = sum( x for x,y in best_centroids)/len(best_centroids)
P_y=sum(y for x,y in best_centroids)/len(best_centroids)
print(int(p_x*10_000))
print(int(P_y*10_000))