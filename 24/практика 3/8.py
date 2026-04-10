f=open('24.8.txt')
data=f.readline().strip().replace('AB','Z')
zindexes=[i for i in range(len(data)) if data[i] == 'Z']
res=[]
for zindex in range(len(zindexes)-20):
    o1=zindexes[zindex+20]-zindexes[zindex]+1+21
    res.append(o1)
print(min(res))