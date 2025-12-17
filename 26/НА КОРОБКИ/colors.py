f=open('26.3.txt')
n=int(f.readline())
all=[]
for s in f:
    lens,clr=s.split()
    all.append([int(lens),clr])
all.sort(reverse=True)
blocks=[]
while all!=[]:
    gift=[all[0]]
    del all[0]
    for anotherbox in all[1:]:
        if gift[-1][0]-anotherbox[0]>=8 and gift[-1][-1] != anotherbox[1]:
            gift.append(anotherbox)
            all.remove(anotherbox)
    blocks.append(gift)
print(len(blocks),len(blocks[0]))