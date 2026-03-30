f=open('26.1.txt')
kolvo=int(f.readline())
boxes=[int(box)for box in f]
boxes.sort(reverse=True)
gift=[boxes[0]]
for boxi in boxes:
    if gift[-1]-boxi>=7:
        gift.append(boxi)

print(len(gift),min(gift))