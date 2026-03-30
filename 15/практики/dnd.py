for A in range(10_000,0,-1):
    for x in range(1,10_000):
        for y in range(1,10_000):
            if ((x<A) and (y<A) and ((x*y)>800)):
                break
        if ((x < A) and (y < A) and ((x * y) > 800)):
            break
    else:
        print(A)
        break