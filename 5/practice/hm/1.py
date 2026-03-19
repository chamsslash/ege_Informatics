def to4(n):
    res=''
    while n:
        res+=str(n%4)
        n//=4
    return res[::-1]
o1=[]
for n in range(1,10_000):
    n4=to4(n)
    n4_1= n4+n4[-3:] if n%3==0 else to4((n%3)*4)+n4
    res=int(n4_1,4)
    if res<1166:
        o1.append(n)
print(max(o1))