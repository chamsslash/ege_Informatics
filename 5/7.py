for mars in range(501,1000):
    n2=bin(mars)[2:]
    n2=str(n2)[::-1]
    n2=n2.lstrip('0') or '0'
    n10=int(n2,2)
    if n10==123:
        print(mars)