def Cel(n,m):
    return n//m
for A in range(10_0,0,-1):
    if all((Cel(x,40)>5) or (not Cel(x,7)>8) or (Cel(x,A)>4) for x in range(1,10_00) for y in range(1,1_000)):
        print(A)