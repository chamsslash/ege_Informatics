for n in range(0,256):
    n2=bin(n)[2:].zfill(8)
    n2=n2.replace('0','x').replace('1','0').replace('x','1')
    n10=int(n2,2)
    n_end=int(n10)-n
    if n_end==-9:
        print(n)