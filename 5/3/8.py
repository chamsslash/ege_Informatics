def to3(i):
    res=''
    while i>0:
        res+=str(i%3)
        i=i//3
    return res[::-1]
for n in range(1,10_000):
    n3=to3(n)
    if n%3==0:
        n3='1'+n3+'02'
    else:
        ostat=to3(n%3*4)
        n3=n3+ostat
    r=int(n3,3)
    if r<208:
        print(n )