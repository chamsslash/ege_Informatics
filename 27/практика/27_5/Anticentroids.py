import math

f=open('27B.txt')
ps=[list(map(float,i.replace(',','.').split())) for i in f]
print(ps)
clusters=[]
eps=1
while ps:
    clusters.append([ps[0]])
    del(ps[0])
    for p in clusters[-1]:
        for p1 in ps[:]:
            if math.dist(p,p1)<eps:
                clusters[-1].append(p1)
                ps.remove(p1)


# ищем АНТИцентроиды
bestie=[[] for i in range(len(clusters))]
for i in range(len(clusters)):
    maxsumdistpercluster=0
    for p in clusters[i]:
        maxsumdist=0
        for p1 in clusters[i]:
            maxsumdist+= math.dist(p,p1)
        if maxsumdistpercluster<maxsumdist:
            maxsumdistpercluster=maxsumdist
            bestie[i]=p
print(len(bestie))
print(len(clusters))
minindex=clusters.index(min(clusters,key=len))
maxindex=clusters.index(max(clusters,key=len))
print(bestie[minindex][0]*10_000,bestie[maxindex][1]*10_000)
# from turtle import *
# k=35
# screensize(2000,2000)
# penup()
# tracer(0)
# colors=['red','green','blue','purple','pink','cyan']
# for i in range (len(clusters)):
#     for x,y in clusters[i]:
#         setpos(x*k,y*k)
#         dot(5,colors[i])
# for x in range(-100,100):
#     for y in range(-100,100):
#         setpos(x*k,y*k)
#         dot(5,'grey')
# done()