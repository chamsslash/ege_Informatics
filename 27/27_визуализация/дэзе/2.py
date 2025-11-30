from turtle import *


f=open("27_1/27B.txt")
f.readline()
k=30
clrs=['pink','orange','green']

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

points=[list(map(float,s.replace(',',".").split())) for s in f]

clusters=[[],[],[]]
for x,y in points:
    if x>-1:
        clusters[1].append([x,y])
    elif x<-1 and y>0:
        clusters[0].append([x,y])
    else:
        clusters[2].append([x,y])

visualise(points)
visualise_clusters(clusters)
best=[[],[],[]]

for i in range(len(clusters)):
    sum_dist_per_cluster=float('inf')
    for x,y in clusters[i]:
        sum_dist_per_point=0
        for x1,y1 in clusters[i]:
            sum_dist_per_point += abs(x1-x) + abs(y1-y)
        if sum_dist_per_point < sum_dist_per_cluster:
            sum_dist_per_cluster=sum_dist_per_point
            best[i]=[x,y]
p_x=sum([x for x,y in best])/len(best)
p_y=sum([y for x,y in best])/len(best)

print(int(p_x*10000))
print(int(p_y*10000))
done()