import math

f=open('27B.txt')
f.readline()
points=[list(map(float,point.replace(',','.').split()))for point in f]
clusters=[]
# класьтеризация
while points:
    clusters.append([points[0]])
    del(points[0])
    for point_in_cluster in clusters[-1]:
        for ost_point in points[:]:
            if math.dist(point_in_cluster,ost_point)<=1:
                clusters[-1].append(ost_point)
                points.remove(ost_point)
    if len(clusters[-1])<=10:
        print('ANOMALY')
        clusters.remove(clusters[-1])
besties=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    msdpc=float('inf')
    for point1 in clusters[i]:
        msd=0
        for point2 in clusters[i]:
            msd+=math.dist(point1[:2],point2[:2])
        if msd<msdpc:
            msdpc=msd
            besties[i]=point1
print(besties)
garmonicheskoe_brbr=[]
for ik in range(len(clusters)):
    garmonicheskoe_brbr.append(len(clusters[ik])/sum([1/brbr for x,y,brbr in clusters[ik]]))
print((sum([x+y for x,y,br in besties]))*10_000)
print(sum(garmonicheskoe_brbr)*10_000)






