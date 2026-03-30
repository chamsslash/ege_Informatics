import math
from turtle import *
f=open('27B.txt')
f.readline()
ps=[list(map(float,i.replace(',','.').split()) )for i in f]
eps=0.5
clusters=[]
# кластеризуем
while ps:
    clusters.append([ps[0]])
    del(ps[0])
    for p in clusters[-1]:
        for p1 in ps[:]:
            if math.dist(p1,p) < eps:
                ps.remove(p1)
                clusters[-1].append(p1)
    if len(clusters[-1])<10:
        print('Anomaly')
        del(clusters[-1])
bestie=[[] for i in range(len(clusters))]
colors=['red','blue','cyan','purple','orange','pink']

for i in range(len(clusters)):
    msdpc=float('inf')
    for o in clusters[i]:
        msd=0
        for o1 in clusters[i]:
            msd += math.dist(o,o1)
        if msd<msdpc:
            msdpc=msd
            bestie[i]=o
            # check
print(bestie)
penup()
screensize(2000,2000)
tracer(0)
k=35
for i in range(len(bestie)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()

