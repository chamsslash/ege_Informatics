import math


def Nod(n,m):
    nod=math.gcd(n,m)
    return nod>math.sqrt(m) and nod>math.sqrt(n)

for A in range(1,10_000):
    if all((not Nod(x,A)) <= (Nod(x,21) <= (not Nod(x,14)))
           for x in range(1,10_000)):
        print(A)

# for A in range(10_000, 0, -1):
#     if all((not Nod(x,A)) <= (Nod(x,21) <= (not Nod(x,14)))
#            for x in range(1,10_000)):
#         print(A)
#         break