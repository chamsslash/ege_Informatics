def t(x,y,z):
    return  ((x==y) and (z==y))
cnt=0
for A in range(1,10_00):
    if all((A>30)<=(t(40,y,A) <= t(x,y,A)) for x in range(1,10_0) for y in range(1,100)):

        cnt+=1
print(cnt)