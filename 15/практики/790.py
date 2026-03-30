for A in range(1,10_000):
    if all(((x<(2*y)) or (((2*x+A)<=3*y) and ((3*y+2*y)>A)))
           for x in range(1,10_000) for y in range(1,10_000)):
        print(A)