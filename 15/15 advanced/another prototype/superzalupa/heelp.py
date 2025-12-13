def treugolnik(n,m,k):
    return (n+m)>k and (n+k)>m and (k+m)>n
for a in range(1,10_000):
    for x in range(1,10_000):
        if (not((treugolnik(x,5,24) == (not(max(x,8)>31))) and treugolnik(x,a,8)))==0:
            break
    else:
        print(a)