f=open('24.6.txt')
res=[]
data=f.readline().strip()
data='A'+data+'A'
aindexes=[i for i in range(len(data)) if data[i]=='A']
for aindex in range(len(aindexes)-4):
    o1=aindexes[aindex+4]-aindexes[aindex]-1
    res.append(o1)
print(max(res))