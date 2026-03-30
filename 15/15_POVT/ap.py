def Del(n,m):
    return n%m==0
b=list(range(60,91))
for a in range(1,10_000):
    if all( (Del(x,a) or ((x in b)<= (not(Del(x,22))))) for x in range(1,10_000)):
        print(a)