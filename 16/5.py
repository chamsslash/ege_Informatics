f=[0]*20_000
g=[0]*20_000
for i in range(18000):
    if i<20:
        g[i]=2*i
    else:
        g[i]=g[i-2]+3
for n in range(18000):
    f[n]=2*(g[n-2]+9)
print(f[16888])