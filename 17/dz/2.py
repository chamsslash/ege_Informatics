f=open('17.2.txt')
res=[]
cnt=0
alls=[int(i)for i in f]
for index in range(len(alls)-1):
    x=alls[index]
    x1=alls[index+1]
    if x>500 or x1>500:
        a=((x1**2)+(x**2))
        cnt+=1
        res.append(a)
print(cnt,max(res))