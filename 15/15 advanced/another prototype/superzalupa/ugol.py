def ugol(a,b,c):
    return (a+b+c) ==180
for a in range(1,10_000):
    for x in range(1,10_000):
        if (ugol(42,a,x+45) == (ugol(a,x,90) and (not(a+30<127))))==False:
            break
    else:
        print(a)
        break