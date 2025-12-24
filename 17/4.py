f=open('dz/17.4.txt')
a=[int(i)for i in f]
res=[]
for s in range(len(a)-2):
    if a[s]>0 or a[s+1]>0 or a[s+2]>0:
        res.append(a[s]+a[s+1]+a[s+2])
print(len(res),min(res))
