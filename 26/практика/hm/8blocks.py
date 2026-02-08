f=open('Задание 7.txt')
box_count=int(f.readline())
boxes=[[int(i.split()[0]), i.split()[1]] for i in f]
boxes.sort(reverse=True)
blocks=[]
while boxes!=[]:
    gift=[boxes[0]]
    boxes.remove(boxes[0])
    for box2 in boxes[:]:
        if gift[-1][0]-box2[0]>=8 and gift[-1][1]!=box2[1]:
            gift.append(box2)
            boxes.remove(box2)
        else:
            continue

    blocks.append(gift)
# самым большим блоком(гифтом) окажется тот что бежал первым по циклу ведь там было в тот момент больше всего коробок
print(len(blocks),len(blocks[0]))
