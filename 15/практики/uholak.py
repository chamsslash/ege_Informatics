def uga(a,b,c):
    return (a+b+c)==180
for A in range(1,10_000):
    if all((uga(47,A,x+40)==(uga(A,x,45) and (not(A+30<156))) for x in range(1,10_000))):
        print(A)
        break