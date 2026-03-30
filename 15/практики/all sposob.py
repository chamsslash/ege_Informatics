for A in range(1,10_000):
    if all((((y*y)<=A)<=(y<=12)) and ((x<10)<=((x*x)< A)) for x in range(1,10_000) for y in range(1,10_000)):
        print(A)