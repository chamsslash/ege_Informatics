f=open('Задание 2.txt')
c=f.readline()
boxes=[int(box) for box in f]
boxes.sort(reverse=True)
gift=[boxes[0]]
for box in boxes[1:]:
    if gift[-1]-box>=5:
        gift.append(box)
print(len(gift),gift[-1])