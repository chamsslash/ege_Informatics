for A in range(1,10_000):
    if all((((x&A)!=0) <= (((x&15)!=0) <= ((x%30)!=0))) for x in range(1,1000)):
        print(A)