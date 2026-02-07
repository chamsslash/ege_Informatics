for n in range(1, 10000):
    n2 = bin(n)[2:]
    s = sum(map(int, n2))

    if s % 2 == 0:
        n2 = n2 + '0'
        n2 = '10' + n2[2:]
    else:
        n2 = n2 + '1'
        n2 = '11' + n2[2:]

    r = int(n2, 2)
    if r >= 256:
        print(n)
        break
