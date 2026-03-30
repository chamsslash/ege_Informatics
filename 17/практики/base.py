f=open("17.8.txt")
data=[int(u)for u in f]
chets=[i for i in data if i%2==0]
max_chet=max(chets)
cnt=0
sums=[]
for i in range(len(data)-1):
    a=data[i]
    b=data[i+1]
    if a+b==max_chet:
        sums.append((a**2)+(b**2))
        cnt+=1
print(cnt,sums)