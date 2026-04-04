f=open('Задание 7.txt')
res=[]
data=f.readline().strip().replace('XZ','I')
iindexes=[i for i in range(len(data)) if data[i]=='I']
for i in range(len(iindexes)-28):
    g4=iindexes[i+28]-iindexes[i]-1+29+2
    res.append(g4)

print(min(res))
