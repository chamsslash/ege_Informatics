def to16(n):
    digits = "0123456789ABCDEF"
    res=''
    while n>0:
        res += str(digits[n%16])
        n//=16
    return res[::-1]
cnt=0
for i in range(1,10000):
    n16=to16(i)
    if i%15==0:
        n16=n16+n16[-2:]
    else:
        ost=i%15
        n16=n16+str(to16(ost*15))
    r=int(n16,16)
    if r<35_000:
        cnt+=1
print(cnt)