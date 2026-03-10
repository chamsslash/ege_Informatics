def t(n,m,k):
    return n+m>k and n+k>m and k+m>n
for A in range(100,1,-1):
    if all(not(    (t(x,4,7)   == (not( max(x,4) >13) )      )     and t(x,A,2)     ) for x in range(1,10_000) for y in range(1,10_000)):
        print(A)
