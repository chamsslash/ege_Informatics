f=open('17.5.txt')
res=[]
a=[int(i)for i in f]
for i in range(len(a)-1):
    if ((a[i]>0 and a[i]**(1/2) %1 ==0) or (a[i+1]>0 and a[i+1]**(1/2) %1==0)):
        print(a[i],a[i]**(1/2))
        res.append(a[i]+a[i+1])
print( len(res),max(res))