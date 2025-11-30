from math import dist
f=open("Задание 2.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
best_centroids= []
min_sum_dist_per_pair=float('inf')
for i in range(len(points)):
    for i1 in range(i+1,len(points)):
        c1,c2=points[i],points[i1]
        sum_dist_for_pair=0
        #перебираем все точки
        for p in points:
            dist1= dist(c1,p)
            dist2=dist(c2,p)
            sum_dist_for_pair+=min(dist1,dist2)
        if sum_dist_for_pair<min_sum_dist_per_pair:best_centroids=[c1,c2];min_sum_dist_per_pair=sum_dist_for_pair
P_x=sum([x for x,y in best_centroids])/len(best_centroids)
P_y=sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_x*10_000),int(P_y*10_000)) 
