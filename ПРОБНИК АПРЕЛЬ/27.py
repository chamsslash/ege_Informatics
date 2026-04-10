import math

f=open('27B.txt')
f.readline()
points=[list(map(float,i.replace(',','.').split())) for i in f]
clusters=[]
eps=1
while points:
    clusters.append([points[0]])
    del(points[0])
    for p1 in clusters[-1]:
        for p2 in points[:]:
            if math.dist(p1,p2) <= eps:
                clusters[-1].append(p2)
                points.remove(p2)
    if len(clusters[-1])<=10:
        print('Animaly')
        del(clusters[-1])
print(len(clusters))
bestie=[[] for i in clusters]
for i in range(len(clusters)):
    msdpc=float('inf')
    for p1 in clusters[i]:
        msd=0
        for p2 in clusters[i]:
            msd+=math.dist(p1,p2)
        if msd <= msdpc:
            msdpc=msd
            bestie[i]=p1


# o1=[len(i) for i in clusters]
# print(o1)
# # наибольший 0й
# # наименьштй -1й
# q1=sum([1 for p in clusters[0] if (0.5 <= math.dist(p,bestie[0]) <= 2.5)])
# q2=sum([1 for p in clusters[-1] if (0.4 <= math.dist(p,bestie[-1]) <= 1.6 )])
# print(q1,q2)
p1=min([math.dist(i,[-2.2,0]) for i in bestie])
p2=max([math.dist(i,[0,-2.0]) for i in bestie])
print(p1*10_000)
print(p2*10_000)
# from turtle import *
# screensize(2000,2000)
# tracer(0)
# k=20
# penup()
# clrs=['blue','red','cyan','yellow']
# for i in range(len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,clrs[i])
# done()


52082111772
269468