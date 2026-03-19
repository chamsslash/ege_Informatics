f=open('Задание 4.txt')
boxes=[]
red_c,blue_c=map(int,f.readline().split())
for i in range(blue_c):

    r,b=map(int,f.readline().split())
    boxes.append([r,'RED'])
    boxes.append([b,'BLUE'])
for ii in f:
    boxes.append([int(ii),'RED'])
boxes.sort(reverse=True)
gift=[boxes[0]]
for boxo in boxes:
    if gift[-1][0]-boxo[0]>=5 and gift[-1][-1]!=boxo[-1]:
        gift.append(boxo)
print(sorted(gift,reverse=True))
print(len(gift))
print(min(gift))