for n in range(1,10000):
    n2=bin(n)[2:]
    summa=0
    for digit in n2:
        summa+=int(digit)
    n2+=str(summa%2)
    summa = 0
    for digit in n2:
        summa+=int(digit)
    n2+=str(summa%2)
    r=int(n2,2)
    if r>22222:
        print(r)