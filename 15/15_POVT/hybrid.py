d=list(range(30,46))
def Del(n,m):
    return n%m==0
for a in range(1,10_000):
    for x in range(1,10_000):

        if (((not(Del(x,7))) and (x not in [52,60,68])) <= (((abs(x-25))<=10) <= (x in d)) or (x&a!=0)) ==0:
            break
    else:
        print(a)
        break
