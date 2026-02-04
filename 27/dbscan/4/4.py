import math

f=open("27B.txt")
f.readline()
clusters=[]
p=[list(map(float,i.replace(",",".").split())) for i in f]
eps=0.25
while p:
    clusters.append([p[0]])
    del p[0]
    for p1 in clusters[-1]:
        for p2 in p:
            if math.dist(p1,p2) < eps:
                clusters[-1].append(p2)
                p.remove(p2)
    if len(clusters[-1])<=10:
        del clusters[-1]
best=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float("inf")
    for x,y in clusters[i]:
        msd=0
        for x1,y1 in clusters[i]:
            msd+=math.dist([x1,y1],[x,y])
        if msd<msdpc:
            msdpc=msd
            best[i]=[x,y]
P_x=sum([x for x,y in best])/len(best)
P_y=sum([y for x,y in best])/len(best)
P_s=sum(len(i)/(3*3) for i in clusters)
print(abs(P_x+P_y)*10000,abs(P_s)*10000)

from turtle import *
penup()
tracer(0)
colors=["red","green","blue","cyan"]
screensize(2000,2000)
k=45
for i in range(len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
done()