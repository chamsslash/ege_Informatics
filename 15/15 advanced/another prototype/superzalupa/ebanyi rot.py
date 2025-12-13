def treugolnik(n,m,k):
    return (n+m)>k and (n+k)>m and (k+m)>n
for a in range(1,1000):
    for x in range(1,1000):
        if (not((treugolnik(x,10,17) == (not(max(x,8)>18)))and treugolnik(x,a,4)))==False:
            break
    else:
        print(a)