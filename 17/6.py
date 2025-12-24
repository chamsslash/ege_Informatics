f=open("17.6.txt")
a=[int(i)for i in f]
res=[]
for i in range(len(a)-1):
    if (a[i]+a[i+1])==max(a):
        res.append(a[i]**2+a[i+1]**2)
print(len(res), max(res))