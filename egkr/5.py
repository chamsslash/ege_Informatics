res=[]
for n in range(1,10_000):
    n2=bin(n)[2:]
    summaed=n2.count('1')
    n2_1=n2+str((summaed%2))
    summaed1 = n2_1.count('1')
    n2_2=n2_1+str((summaed1%2))
    r=int(n2_2,2)
    if r>253:
        res.append(n)
print(min(res))