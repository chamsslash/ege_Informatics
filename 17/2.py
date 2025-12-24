f=open("17.2.txt")
a=[]
for s in f:
    a.append(int(s))
s=[]
for i in  range(len(a)-1):
    if a[i]>1234 or a[i+1]>1234:
        s.append(a[i]**2+a[i+1]**2)

print(len(s),max(s))