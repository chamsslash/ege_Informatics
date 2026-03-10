for A in range(10_000,0,-1):
    if not any((x <A) and (y <A) and ((x*y)>1600) for x in range(1,10_000) for y in range(1,10_000)):
        print(A)
