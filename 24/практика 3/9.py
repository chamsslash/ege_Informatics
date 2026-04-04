f=open('24.9.txt')
res=[]
data=f.readline().strip().replace('AB','Z')
zindexes=[i for i in range(len(data)) if data[i]=='Z']
for i in range(len(zindexes)-22):
    o1=zindexes[i+22]-zindexes[i]-1+2+21
    res.append(o1)
print(max(res))