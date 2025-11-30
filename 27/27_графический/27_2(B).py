from math import *
f=open("27_B_2.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]# clusters=[[],[]]
k=3 #количество кластеров
clusters=[[] for _ in range(k)]
best_centroids=[[] for _ in range(k)]

for x,y in points:
    if x<10:
        clusters[0].append([x,y])
    elif x>21:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
for i in range(k):
    min_sum_dist=10**100
    for x1,y1 in clusters[i]:
        sum_dist=0
        for x2,y2 in clusters[i]:
            sum_dist += dist([x1,y1],[x2,y2])
        if sum_dist<min_sum_dist:
            min_sum_dist=sum_dist
            best_centroids[i]=(x1,y1)
print(best_centroids)
P_X = sum([x for x,y in best_centroids])/len(best_centroids)
P_Y = sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_X*10_000),int(P_Y*10_000)) #или //1