import math
from fnmatch import fnmatch
from math import *
f=open('27_B.txt')
data=[[float(i.split()[0].replace(',','.')),float(i.split()[1].replace(',','.')),i.split()[2]]for i in f  ]
data1=data[:]
clusters=[]
while data:
    clusters.append([data[0]])
    del data[0]
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if math.dist(p1[:2],p2[:2]) < 2:
                clusters[-1].append(p2)
                data.remove(p2)
    if len(clusters[-1])<=10:
        print('Anomaly')
print(clusters)
besties=[[] for i in range(len(clusters))]

for i in range(len(clusters)):
    msdpc=float('inf')
    for p1 in clusters[i]:
        msd=0
        for p2 in clusters[i]:
            msd+=math.dist(p1[:2],p2[:2])
        if msdpc>msd:
            besties[i]=p1
            msdpc=msd
print(besties)
print([len(cl) for cl in clusters])
red_giants=[[x,y,dop]for x,y,dop in data1 if fnmatch(dop,'Y?III')]
print("red_giants",red_giants)
# print(min([math.dist(besties[-1][:2],red_giant[:2])for red_giant in red_giants])*10_000)
# print(max([math.dist(besties[-1][:2],red_giant[:2])for red_giant in red_giants])*10_000)
# 4940.379944002089
# 74302.58474932075
print(sum([1 for i in clusters for j in i if fnmatch(j[2],'Z?I')]))
yellow_supergiants=[[]for i in range(len(clusters))]
for i in range(len(clusters)):
    for point in clusters[i]:
        if fnmatch(point[2],'Z?I'):
            yellow_supergiants[i].append(point)

print("yellow_supergiants",yellow_supergiants)
print('yel_len',[len(i) for i in yellow_supergiants ])
res=[]
# for ye_cluster in yellow_supergiants:
#     max_dist_ye=float('inf')
#     for point in ye_cluster:
#         for point2 in ye_cluster:
#             if point[:2]!=point2[:2]:
#                 md=math.dist(point[:2],point2[:2])
#                 if md<max_dist_ye:
#                     max_dist_ye=md
#     res.append(max_dist_ye)
o1=[math.dist(p1[:2],p2[:2]) for i in range(len(yellow_supergiants)) for p1 in yellow_supergiants[i] for p2 in yellow_supergiants[i] if p1!=p2]
print(res)
print(min(o1)*10_000)
# print(min(res)*10_000)
print(math.dist(besties[1][:2],besties[0][:2])*10_000)
from turtle import *
penup()
screensize(2000,2000)
tracer(0)
k=10
left(90)
clrs=['red','green','blue','cyan','orange','black','purple','brown','yellow','aquamarine']
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot()
for i in range(len(clusters)):
    for x,y,dop in clusters[i]:
        setpos(x * k, y * k)
        dot(k,clrs[i])

done()