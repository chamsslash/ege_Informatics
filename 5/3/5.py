for n in range(1,10_000):
    n1=n-(n%4)
    n2=bin(n1)[2:]
    summ=sum(map(int,n2))
    n2=n2+str(summ%2)
    summ=sum(map(int,n2))
    n2 = n2 + str(summ % 2)
    r=int(n2,2)
    if r<80:
        print(n)
