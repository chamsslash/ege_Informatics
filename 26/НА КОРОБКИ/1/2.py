f=open('Задание 2.txt')
c=int(f.readline()
)
boxes=[int(i)for i in f]
boxes.sort(reverse=True)
gift=[boxes[0]]

for box in boxes:
    if gift[-1]-box>=11:
        gift.append(box)
print(len(gift),min(gift))