f=open('Задание 3.txt')
box_c,tape_c=map(int,f.readline().split())
boxes=[]
tapes=[]
for _ in range(tape_c):
    box,tape=map(int,f.readline().split())
    boxes.append(box)
    tapes.append(tape)
for __ in f:
    boxes.append(int(__))
    tapes.append(0)
gift=[]
boxes.sort(reverse=True)
tapes.sort(reverse=True)

for boxii in boxes:
    if len(gift)==0 and boxii in tapes:
        gift=[boxii]
    if len(gift)!=0 and boxii in tapes and gift[-1]-boxii>=9:
        gift.append(boxii)
minis=10_000
for av_min in boxes:
    if av_min in tapes and minis>av_min:
        minis=av_min
print(len(gift),(max(gift)-minis))
print(max(gift))
print(minis)