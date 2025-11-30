from math import dist
f= open("task27_1/27A.txt")
f.readline()
points = [list(map(float,s.replace(",",".").split())) for s in f]
k=2
clusters=[[] for _ in range(k)]
best=[[] for _ in range(k)]
for x,y in points:
    if x>2:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
for i in range(len(clusters)):
    min=float('inf')
    for x1,y1 in clusters[i]:
        sum_for_point=0
        for x2,y2 in clusters[i]:
            sum_for_point+=dist([x1,y1],[x2,y2])
        if min>sum_for_point:min=sum_for_point;best[i]=[x1,y1]
print(best)
print(int(sum([x for x,y in best])/len(best)*10_000))
print(int(sum([y for x,y in best])/len(best)*10_000))