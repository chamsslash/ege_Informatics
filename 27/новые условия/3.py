import math

f=open("27_3.txt")
f.readline()
dots=[list(map(float,(i.replace(',','.')).split())) for i in f]
clust=[]
while dots:
    clust.append([dots[0]])
    del dots[0]
    for p in clust[-1]:
        for p1 in dots[:]:
            if math.dist(p1,p) < 1:
                clust[-1].append(p1)
                dots.remove(p1)
    if len(clust[-1])<=10:
        del clust[-1]
print(len(clust))
bestie=[[]for i in range(len(clust))

]
for i in range(len(clust)):
    msdpc=float('inf')
    for a  in clust[i]:
        msd=0
        for b in clust[i]:
            msd+=math.dist(a,b)
        if msd<msdpc:
            msdpc=msd
            bestie[i]=a
o1=[math.dist(bestie[i],[0,0])for i in range(len(clust))]
print(min(o1),max(o1))