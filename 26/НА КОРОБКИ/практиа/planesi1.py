f=open('26.6.txt')
c,p=map(int,f.readline().split())
res=[]
commands=sorted([int(f.readline())for i in range(c)],reverse=True)
planes=sorted([int(f.readline()) for i in range(p)],reverse=True)
for comm in commands:
    for plane in planes:
        if comm*2<=plane:
            res.append(comm)
            planes.remove(plane)
            break
print(res)
print(len(res))
print(max(res))