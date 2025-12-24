f=open("17.5.txt")
als=[int(i)for i in f]
res=[]
cnt=0
for index in range(len(als)-1):
    x=als[index]
    y=als[index+1]
    if x**2+y**2>80 and (x**2+y**2)%2==0:
        res.append([x+y,max(x,y)])
        cnt+=1
print(cnt,min(res)[1])