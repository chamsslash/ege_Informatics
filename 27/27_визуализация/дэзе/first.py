from turtle import *
from math import dist, sqrt
f=open("27_1/27A.txt")
f.readline()
clrs=['pink','orange']
points=[list(map(float,s.replace(',',".").split())) for s in f]
k=30
penup()
tracer(0)
screensize(2000,2000)
def visualise(points1):
    for xk,yk in points1:
        setpos(xk * k, yk * k)
        dot(5,'blue')
    for xkk in range(-10,10):
        for ykk in range(-10,10):
            setpos(xkk*k,ykk*k)
            if xkk==0 or ykk ==0:
                dot(5,'red')
            else:
                dot()
    
def visualise_clusters(clusters1):
    for ix in range(len(clusters1)):
        for xt,yt in clusters1[ix]:
            setpos(xt*k,yt*k)
            dot(5,clrs[ix])

clusters=[[],[]]
for x,y in points:
    if y>0:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
visualise(points)
visualise_clusters(clusters)


best=[[],[]]
for i in range(len(clusters)):
    min_dist_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_dist_per_point=0
        for x1,y1 in clusters[i]:
            sum_dist_per_point+=sqrt(abs(x-x1)**2+abs(y-y1)**2 )    
        if min_dist_per_cluster>sum_dist_per_point:min_dist_per_cluster=sum_dist_per_point;best[i]=[x,y]
P_X=sum([x for x,y in best])/len(best) #СРЕД АРИФМ
P_Y=sum([y for x,y in best])/len(best)
print(int(P_X*10000))
print(int(P_Y*10000))
done()
