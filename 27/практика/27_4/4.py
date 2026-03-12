import math

f=open('27B.txt')
f.readline()
ps=[list(map(float,i.replace(',','.').split())) for i in f]
eps=1
clusters=[]
while ps:
    clusters.append([ps[0]])
    del(ps[0])
    for p in clusters[-1]:
        for p1 in ps[:]:
            if math.dist(p,p1) < eps:
                clusters[-1].append(p1)
                ps.remove(p1)
    if len(clusters[-1])<10:
        print('Anomaly')
        del(clusters[-1])
print(clusters)
print(len(clusters))
besties=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p1 in clusters[i]:
        msd=0
        for p2 in clusters[i]:
            msd+=math.dist(p1,p2)
        if msd<msdpc:
            msdpc=msd
            besties[i]=p1
print(besties)
o1=min([math.dist(i,[-1.2,0])for i in besties])
o2=max([math.dist(i,[0,-1.0])for i in besties])
print(o1,o2)

max_index=clusters.index(max(clusters,key=len))
min_index=clusters.index(min(clusters,key=len))
o3=sum([1 for p in clusters[max_index] if 0.6 <=math.dist(besties[max_index],p) <=1.8])
o4=sum([1 for p in clusters[min_index] if 0.3 <=math.dist(besties[min_index],p) <= 1.6])
print(o3,o4)


from turtle import *
k=35
screensize(2000,2000)
penup()
tracer(0)
colors=['red','green','blue','purple','pink','cyan']
for i in range (len(clusters)):
    for x,y in clusters[i]:
        setpos(x*k,y*k)
        dot(5,colors[i])
for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*k,y*k)
        dot(5,'grey')
done()