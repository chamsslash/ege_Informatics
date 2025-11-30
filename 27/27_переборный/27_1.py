from math import *

f= open("27A_1.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
# k=2
best_centroids= []
min_sum_dist= float("inf")
for i in range(len(points)):
    for j in range(i+1,len(points)):
        c1,c2=points[i],points[j]
        sum_dist=0
        for p1 in points:
            #Все растояния от точки
            dist1= dist(c1,p1)
            dist2=dist(c2,p1)
            sum_dist+=min(dist1,dist2)
        if min_sum_dist>sum_dist:
            min_sum_dist=sum_dist
            best_centroids=[c1,c2]
P_x=sum([x for x,y in best_centroids])/len(best_centroids)
P_y=sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_x*10_000),int(P_y*10_000))