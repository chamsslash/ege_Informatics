import math

f=open("27_2.txt","r")
f.readline()
dots=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
while dots:
    clusters.append([dots[0]])
    del dots[0]
    for p in clusters[-1]:
        for p1 in dots[:]:
            if math.dist(p1,p) < 1:
                clusters[-1].append(p1)
                dots.remove(p1)
    if len(clusters[-1]) <= 10:
        del clusters[-1]
print(len(clusters))
best=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float("inf")
    for a in clusters[i]:
        msd=0
        for b in clusters[i]:
            msd+=math.dist(a,b)
        if msd<msdpc:
            best[i]=a
            msdpc=msd
dist_bests=[math.dist(best[i],best[1-i])for i in range(len(best))]
maxi=[math.dist(best[i],dot)for i in range(len(clusters)) for dot in clusters[i]]
print(dist_bests,max(maxi))
