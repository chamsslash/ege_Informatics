for i in range(1,10_000):
    n2=bin(i)[2:]
    if n2.count('1')%2==0:
        n2=n2+'0'
        n2 = '10' + n2[2:]
    else:
        n2=n2+'1'
        n2= '11'+ n2[2:]
    r=int(n2,2)
    if r>=16:
        print(i)
        break
