for A in range(0,10_000):
    for x in range(1,10_000):
        for y in range(1,10_000):
            if ((x>=30) or (x*y<A) or (x<15*y))==0:
                break
        if ((x >= 30) or (x * y < A) or (x < 15 * y)) == 0:
            break
    else:
        print(A)