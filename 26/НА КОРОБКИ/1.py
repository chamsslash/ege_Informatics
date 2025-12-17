f= open("26.1.txt")
n=int(f.readline())

all=[int(x) for x in f]
all.sort(reverse=True)
print(all)
gift=[all[0]]
for x in all[1:]:
    if gift[-1]-x>=3:
        gift.append(x)
print(len(gift),min(gift))