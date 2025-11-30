from math import *

f= open("27A_2.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
# k=2
best_centroids= []
min_dist= float("inf")
for i in range(len(points)):
    for j in range(i+1,len(points)):
        sum_dist=0
        for p1 in points:
            sum_dist+= min(dist(points[i],p1),dist(points[j],p1))
        if sum_dist<min_dist:
            min_dist>sum_dist
            min_dist=sum_dist
            best_centroids=[points[i],points[j]]
P_x=sum([x for x,y in best_centroids])/len(best_centroids)
P_y=sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_x*10_000),int(P_y*10_000))
