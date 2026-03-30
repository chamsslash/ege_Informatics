d=list(range(30,46))
res=[]
def Del(n,m):
    return n%m==0
for a in range(1,10_000):
    for x in range(1,10_000):
        if ((not(Del(x,6)) and (x not in [45,50,55,60]) ) <= ((abs(x-15)<=5) <= (x in d)) or ((x&a)!=0))==0:
            break
    else:
        print(a)
        res.append(a)
print(min(res))