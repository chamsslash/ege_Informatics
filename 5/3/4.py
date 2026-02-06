for n in range(1, 10_000):
    cur = n
    for _ in range(3):
        n2 = bin(cur)[2:]
        s = sum(map(int, str(cur)))
        n2 += str(s % 2)
        cur = int(n2, 2)
    r = cur
    if r > 1234:               
        print(r)
        break
