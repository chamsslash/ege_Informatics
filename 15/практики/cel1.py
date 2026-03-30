def Cel(n,m):
    return n//m
for A in range(1,10_000):
    if all(((Cel(x,50)>3) or (not(Cel(x,13)>3)) or (Cel(x,A)>6)) for x in range(1,10_000)):
        print(A)
        break
