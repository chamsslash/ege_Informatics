f=open('17.txt')
cnt=0
res=[]
data=[int(i) for i in f]
min_23=min([i for i in data if (i%23)==0])
for i in range(len(data)-1):
    a=data[i]
    b=data[i+1]
    if ((a%min_23)==0 or (b%min_23)==0):
        res.append(a+b)
        cnt+=1

print(cnt,max(res))