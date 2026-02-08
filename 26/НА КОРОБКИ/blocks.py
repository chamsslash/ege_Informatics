f=open('26.2.txt')
n=int(f.readline())
all=[int(x) for x in f]
blocks=[]
while all!=[]:
    full=[all[0]]
    del all[0]
    for box in all:
        if full[-1]-box>=5:
            full.append(box)
            all.remove(box)
    blocks.append(full)
print(len(blocks),len(blocks[0]))
# по факту задачка на много гифтов