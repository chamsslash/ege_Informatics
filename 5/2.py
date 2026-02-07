for n in range(0,256):

    n2 = bin(n)[2:].zfill(8).replace('0', 'x').replace('1', '0').replace('x', '1')
    n10=int(n2,2)
    reversed_n10=(str(n10))[::-1]
    if reversed_n10=='351':
        print(n)
        break
