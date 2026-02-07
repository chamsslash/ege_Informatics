f=open('24.5.txt')
n=f.readline().strip()
res=[]
for a1 in range(len(n)):
    if n[a1] not in '24680':
        continue
    cnt=0
    for a2 in range(a1+1,len(n)):
        if n[a2] in '24680':break
        if n[a2]=='H':cnt+=1
        if cnt==30:
            res.append(a2-a1+1)

        if cnt>30:break
print(max(res))
