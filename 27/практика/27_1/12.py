import math
from turtle import *
colors=['red','blue','cyan','purple','orange','pink']
f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
# кластеризуем

eps=1
clusters=[]
while points:
    clusters.append([points[0]])
    del(points[0])
    for clu_point in clusters[-1]:
        for point2 in points[:]:
            if math.dist(clu_point,point2)<eps:
                clusters[-1].append(point2)
                points.remove(point2)

    if len(clusters[-1])<5:
        print("Anomaly")
        del(clusters[-1])
# print(clusters)


# бест центроидс
besties=[[],[],[],[],[]]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p in clusters[i]:
        msd=0
        for p1 in clusters[i]:
            msd+= math.dist(p1,p)
        if msd<msdpc:
            besties[i]=p
            msdpc=msd
print(besties)
print(abs((sum(centroid[0] for centroid in besties))/len(besties)*10_000)//1)
print(abs((sum(centroid[1] for centroid in besties))/len(besties)*10_000)//1)

# checkup
penup()
tracer(0)
k=35
screensize(2000,2000)
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])


done()