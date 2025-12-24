f=open('dz/17.1.txt')
s=[]
a=[int(i) for i in f]
for i in range(len(a)-1):
    if a[i]%11==0 and a[i+1]%11==0:
        s.append(a[i]+a[i+1])
print(len(s),min(s))