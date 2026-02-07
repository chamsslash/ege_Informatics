for n in range(1,10_000):
    n2=bin(n)[2:]
    if n%3==0:
        n2=n2+n2[-3:]
    else:
        ost = (n % 3) * 3
        n2 = n2 + bin(ost)[2:]

    n10=int(n2,2)
    if n10>54:
        print(n10)
        break