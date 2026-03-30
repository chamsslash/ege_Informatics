def to3(n):
    res=''
    while (n):
        res += str(n%3)
        n=n//3
    return res[::-1]
res=[]
for n in range(1,10_000):
    n3=to3(n)
    n3_1= n3 + n3[:2] if (n%3==0) else n3+to3((n%3)*7)
    r=int(n3_1,3)
    if r>260:
        res.append(r)
print(min(res))