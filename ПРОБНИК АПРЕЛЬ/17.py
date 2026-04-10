f=open('17.txt')
res=[]
cnt=0
data=[int(i) for i in f]
max7=max([i for i in data if str(i)[-1]=='7'])
for i in range (len(data)-2):
    a=data[i]
    b=data[i+1]
    c=data[i+2]
    troy=sorted([a,b,c])
    if (troy[-1]*troy[1])>(troy[0]*max7):
        res.append(sum(troy))
        cnt+=1
print(cnt)
print(abs(min(res)))