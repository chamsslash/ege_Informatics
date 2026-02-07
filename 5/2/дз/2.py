for n in range(1,10000):
    n2=bin(n)[2:]
    summa=sum(map(int,n2))
    n2=n2+str(summa%2)
    summa=0
    summa=sum(map(int,n2))

    n2=n2+str(summa%2)
    n10=int(n2,2)
    if n10>720:
        print(n10)
        break