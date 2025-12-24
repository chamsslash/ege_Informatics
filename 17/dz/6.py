f=open('17.6.txt')
als=[int(i)for i in f]
res=[]
cnt=0
for index in range(len(als)-1):
    x=als[index]
    y=als[index+1]
    if abs(x)+abs(y)>650:
        res.append(max(x,y))
        cnt+=1
print(cnt,max(res))