f=open("Задание 5.txt")
n=f.readline().strip()
res=[]
for a1 in range(len(n)):
    cnt=0
    if n[a1] not in '13579':
        continue
    for a2 in range(a1+1,len(n)):
        if n[a2] == 'r':
            cnt+=1
        if n[a2]  in '13579': break
        if cnt>58:
            break
        if cnt==58:
            res.append([a2-a1+1])
print(max(res))