f=open('26.3.txt')
box_c,zam_c=map(int,f.readline().split())
boxes=[]
zamochks=[]
for i in range(zam_c):
    box,zam=map(int,f.readline().split())
    boxes.append(box)
    zamochks.append(zam)
for box in f:
    boxes.append(int(box))
    zamochks.append(0)
boxes.sort(reverse=True)
gift=[]
for box in boxes:
    if len(gift)==0 and box in zamochks:
        gift=[box]
    elif ((gift[-1]-box>=6) and ( box in zamochks)):
        gift.append(box)

print(len(gift))
print(min(gift))