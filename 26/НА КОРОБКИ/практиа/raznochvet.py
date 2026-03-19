f=open('26.4.txt')
r_c,b_c=map(int,f.readline().split())
bxs=[]
for i in range(b_c):
    red,blue=map(int,f.readline().split())
    bxs.append([red,'red'])
    bxs.append([blue,'blue'])
for box in f:

    bxs.append([int(box),'red'])
bxs.sort(reverse=True)
print(bxs)
gift=[bxs[0]]
for o in bxs:
    if (gift[-1][0]-o[0])>=5 and gift[-1][1]!=o[1]:
        gift.append(o)
print(len(gift))
print(min(gift))