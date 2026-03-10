def Inf(n,m):
    return n%m==8
for A in range(1,10_000):
    if all(Inf(x,A) <= ((x%180==0) and ((x%150)!=0)) for x in range(1,10_000)):
        print(A)