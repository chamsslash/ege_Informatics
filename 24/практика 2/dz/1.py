f=open('1.txt')
n=f.readline()
maxi=float('inf')
ks=[i for i,k in enumerate(n) if k=='K']
for k_i in range(len(ks)-309):
    a=ks[k_i+309]-ks[k_i]+1
    maxi=min(a,maxi)
print(maxi)
