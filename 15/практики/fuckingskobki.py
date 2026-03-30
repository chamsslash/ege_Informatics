def t(a,b,c):
    return a+b>c and a+c>b and b+c>a
for A in range(1,10_000):
    if all(not( (t(x,11,24) == (not(max(x,7)>32))  ) and t(x,A,7)   ) for x in range(1,10_000)):
        print(A)
