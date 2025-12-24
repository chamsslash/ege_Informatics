f=open('17.6.txt')
res=[]
cnt=0
als=[int(i) for i in f]
for index in range(len(als)-1):
    x=als[index]
    y=als[index+1]
    if (x**0.5)%1==0 or (y**0.5)%1==0 :
        res.append(x+y)
        cnt+=1
print(cnt,max(res))