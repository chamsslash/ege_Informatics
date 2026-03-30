def to4(n):
    res=''
    while n:
        res+=str(n%4)
        n//=4
    return res[::-1]
o1=[]
for i in range(1,10_000):
    i2=bin(i)[2:]
    i4=to4(i)
    i2_1= ('10' + i2[2:] + '0') if ((int(i4[0])%2)==0) else ('1'+i2[:-2]+'0'+i2[-1])
    res=int(i2_1,2)
    if i>490:
        o1.append(res)
print(min(o1))

