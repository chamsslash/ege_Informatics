from math import  *
for lenn in range(1,10_000):
    N=106+980
    i=ceil((log2(N)))
    V1=ceil((i*lenn)/8)
    v385=(V1*385 )/2**10
    if v385<136:
        print(lenn)