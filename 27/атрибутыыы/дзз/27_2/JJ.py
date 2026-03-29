import math

f=open('27A.txt','r')
f.readline()
pointo=[list(map(int,i.replace(',','.'))) for i in f]
clusters=[]
while pointo:
    clusters.append([pointo])
    del pointo[0]
    for p in clusters[-1]:
        for p1 in pointo[:]:
            if math.dist(p1,p) <=0.5:
                clusters[-1].append(p1)
                pointo.remove(p1)
    if len(clusters[-1])<=10:
        print('Anomaly')
        del clusters[-1]
dev=[]
besti=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    dispers=[]
    srr=sum([w for x,y,w in clusters[i]])/len(clusters[i])
    msdpc=float('inf')
    for o1 in clusters[i]:
        msd=0
        for o2 in clusters[i]:
            msd+= math.dist(o1,o2)
        if msd<msdpc:
            msdpc=msd
            besti[i]=o1
        dispers.append((o1[-1]-srr)**2)
    dis=sum(dispers)/len(dispers)
    dev.append(dis**0.5)
cnt=0
print(besti)
unistars=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    sr=sum([w for x,y,w in clusters[i]])/len(clusters[i])
    for x,y,w in clusters[i]:
        if abs(w-sr)>1.5*dev[i]:
            cnt += 1
print(sum(x+y for x,y,w in besti)*10_000)
print(cnt)