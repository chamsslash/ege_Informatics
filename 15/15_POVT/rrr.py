def Del(n,m):
    return n%m==0
cnt=0
b=list(range(100,121))
for a in range(1,10_000):
    for x in range(1,10_000):
        if  ((x in b) <= (((Del(x,35)) == (Del(x,a))) or Del(x,a)))==0:
            break
    else:
        cnt+=1
        print(a)
print(cnt)