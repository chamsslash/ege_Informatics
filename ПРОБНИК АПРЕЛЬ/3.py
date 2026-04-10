ooo=[]
for n in range(1000,9999+1):
    ns=str(n)
    ds=[int(d) for d in ns]
    S=sum(ds)
    M=max(ds)
    N=min(ds)
    p1=S-M
    p2=S-N
    o1=max(p1,p2)
    o2=min(p1,p2)
    res=f'{o1}{o2}'
    if (res)=='2214':
        ooo.append(n)
print(min(ooo))

