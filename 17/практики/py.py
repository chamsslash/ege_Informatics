f=open("17.7.txt")
data=[int(i)for i in f]
minel=min(data)
sums=[]
cnt=0
for i in range(len(data)-1):
    a=data[i]
    b=data[i+1]
    if (a%442==minel or b%442==minel):
        sums.append(a+b)
        cnt+=1
print(cnt,max(sums))