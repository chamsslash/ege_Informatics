f=open('Задание 1.txt')
box_c=int(f.readline())
boxes=[int(i)for i in f]
boxes.sort(reverse=True)
gift=[boxes[0]]
for box in boxes:
    if gift[-1]-box>=5:
        gift.append(box)
print(len(gift))
print(min(gift))
