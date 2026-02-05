def f(n):
    if n <= 3:return n**3
    if n%2==0: return n+2+8*f(n-2)
    if n%2!=0: return 17*n+f(n-3)-f(n-4)+8
cnt=0
for i in range(134,929):
    if f(i)%6==0: cnt+=1

print(cnt)
