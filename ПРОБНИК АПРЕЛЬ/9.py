f=open('9.txt')
res=[]
num=0
for line in f:

    num+=1
    data=list(map(int,line.split()))
    povt=[d for d in data if data.count(d)>1]
    nepovt=[d for d in data if data.count(d)==1]
    if ((len(set(povt))==1) and (len(set(nepovt))==4 )and (len(povt)==3) and (sum(povt)<sum(nepovt))):
        res.append(num)
res.sort(reverse=True)
print(res[:5])
print(max(res))

