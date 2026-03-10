f=open('17.12.txt')
data=[ int(i) for i in f]
max75=max([i for i in data if str(i)[-2:]=='75'])
sums=[]
cnt=0
for i in range(len(data)-2):
    a=data[i]
    b=data[i+1]
    c=data[i+2]
    if ((len(str(a))==5) + (len(str(b))== 5) +(len(str(c))==5)) >= 1:
        cnt+=1
        sums.append(a+b+c)
print(cnt,max(sums))
