f=open('26.2.txt')
k=int(f.readline())
boxes=[int(i)for i in f]
boxes.sort(reverse=True)
gift=[boxes[0]]
for boxi in boxes:
    if gift[-1]-boxi>=6:
        gift.append(boxi)
print(len(gift))
print(min(gift))