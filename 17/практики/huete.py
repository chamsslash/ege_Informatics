f=open('17.9.txt')
data=[int(i)for i in f]
ends7=[i for i in data if str(i)[-1]=='7' and i!=7]
min7=min(ends7)
cnt=0
sums=[]
for i in range(len(data)-1):
    a=data[i]
    b=data[i+1]
    if a%min7==0 and b%min7==0:
        sums.append(a+b)
        cnt+=1
print(cnt,max(sums))