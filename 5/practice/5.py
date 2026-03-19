def to3(n):
    res=''
    while n:
        res+= str(n%3)
        n//=3
    return res[::-1]
res=[]
for n in range(1,1000):
    n3=to3(n)
    if n%3==0:
        n3+=n3[-2:]
    else:
        n3+=to3((n%3)*5)
    r=int(n3,3)
    if r> 178:
        res.append(r)
print(min(res))