def to5(n):
    res=''
    while n:
        res += str(n%5)
        n=n//5

    return res[::-1]
res=[]
for n in range(1,1_000):

    n5=to5(n)
    if n%10==0:
        n5+=n5[-2:]
    else:
        n5=to5((n%10)*3)+n5
    r=int(n5,5)
    if r<281:
        print(n)
        res.append(n)
print(max(res))