for n in range(1,10_000):
    n2=bin(n)[2:]
    n2=n2+n2[-1]
    n2 = n2 + str(n2.count('1') % 2)
    n2=n2+str(n2.count('1')%2)
    n10=int(n2,2)
    if n10>144:
        print(n)
        break