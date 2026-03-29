import math

f=open('27A.txt')
f.readline()
clusters=[]
points=[list(map(float,i.replace(',','.').split())) for i in f]
while points:
    clusters.append([points[0]])
    del(points[0])
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) <= 1:
                clusters[-1].append(p2)
                points.remove(p2)
    if len(clusters[-1])<=10:
        del(clusters[-1])
        print('ANOALY')
besties=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for pp in clusters[i]:
        msd=0
        for pp1 in clusters[i]:
            msd+=math.dist(pp[:2],pp1[:2])
        if msd<msdpc:
            msdpc=msd
            besties[i]=pp
medisi=[]
for ik in range(len(clusters)):
    brs=[]
    med=0
    for x,y,brbr in clusters[ik]:
        brs.append(brbr)
    brs.sort()
    if len(brs)%2!=0:
        med=brs[len(brs)//2]
    else:
        med=((brs[len(brs)//2]+brs[(len(brs)//2)-1])/2)
    medisi.append(med)

print(sum([x+y for x,y,brbr in besties])*10_000)

print(sum(medisi)*10_000)
