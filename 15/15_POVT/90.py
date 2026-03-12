def Del(n,m):
    return n%m==0
b=list(range(45,91))
for a in range(1,10_000):
    for x in range(1,10_000):
        if (Del(x,52) and (not((x not in b) or (Del(x,a)))))==1:
            break
    else:
        print(a)
