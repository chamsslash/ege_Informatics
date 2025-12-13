def Del(n,m):
    return n % m == 0
b=list(range(60,91))
for a in range(1,1000):
    for x in range(1,1000):
        if ((Del(x,a)) or ((x in b) <= (not(Del(x,22)))))==False:
            break
    else:
        print(a)