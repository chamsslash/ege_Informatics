from math import dist
f=open("Задание 1.txt")
f.readline()
points=[list(map(float,s.replace(",",".").split())) for s in f]
best_centroids= []
min_sum_dist_per_pair=float("inf")
for i in range(len(points)):
        for j in range(i+1,len(points)):
            c1,c2=points[i],points[j]
            sumdist=0
            #берем точку
            for p in points:
                dist1= dist(c1,p)
                dist2=dist(c2,p)
                sumdist+=min(dist1,dist2)
            if min_sum_dist_per_pair>sumdist:min_sum_dist_per_pair=sumdist;best_centroids=[c1,c2]
P_x=sum([x for x,y in best_centroids])/len(best_centroids)
P_y=sum([y for x,y in best_centroids])/len(best_centroids)
print(int(P_x*10_000),int(P_y*10_000))