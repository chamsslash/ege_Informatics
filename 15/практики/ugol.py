def u(a,b,c):
    return ( a+b+c )== 180
for A in range(1,10000):
    if all(u(27,A,x+60) == u(A,x,45) and (not(A+15<112)) for x in range(1,10_000)):
        print(A)
