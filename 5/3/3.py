for n in range(1,10_000):
    n2=bin(n)[2:]
    if n%2==0:
        n2=n2+bin(sum(map(int,n2)))[2:]
    else:
        n2='1'+n2+'00'
    r=int(n2,2)
    if r>543:
        print(n)
        break