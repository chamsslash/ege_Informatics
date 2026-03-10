f=open('ga.txt')
data=[int(i)for i in f]
maxis123=[i for i in data if str(i)[-3:]=='123']
m=max(maxis123)
print(maxis123)
cnt=0
sums=[]
for i in range(len(data)-2):
    a=data[i]
    b=data[i+1]
    c=data[i+2]
    # (((len(str(a)))+(len(str(b)))+(len(str(c))))==8)
    if (((len(str(a))==3)+(len(str(b))==3)+(len(str(c))==3))==2) and (a+b+c)<=m:
        sums.append(a+b+c)
        cnt+=1
print(cnt,max(sums))

