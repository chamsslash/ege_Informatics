f=open('17.3.txt')
a=[int(i) for i in f]
res=[]
for i in range(len(a)-1):
    if a[i]*a[i+1]%74==0:
        res.append(a[i]+a[i+1])
print(len(res),max(res))