f=open('17.1.txt')
mods=[]
cnt=0
alls=[int(x) for x in f]
for i in range(len(alls)-1) :
    x=alls[i]
    y=alls[i+1]
    if x%8==0 and y%8==0:
        min_mod=abs(x-y)
        cnt+=1
        mods.append(min_mod)
print(cnt,min(mods))