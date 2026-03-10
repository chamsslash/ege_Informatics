def Del(n,m):
    return n % m == 0
for A in range(1,10_000):
    for x in range(1,10_000):
        if ((Del(x,13)<=(not Del(x,21))) or (x+A>=750))==0:
            break
    else:
        print(A)