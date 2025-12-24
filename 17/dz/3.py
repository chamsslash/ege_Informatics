f=open('17.3.txt')
res=[]
cnt=0
als=[int(i) for i in f]
for index in range(len(als)-2):
    x=als[index]
    y=als[index+1]
    z=als[index+2]
    if (x<0 or y<0 or z<0):
        a=x+y+z
        cnt+=1
        res.append(a)
print(cnt,min(res))