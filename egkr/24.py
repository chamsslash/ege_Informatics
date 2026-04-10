f=open('24.txt')
data=f.readline().strip().replace('BC','Z')
data='Z'+data+'Z'
res=[]
zindexes=[i for i in range(len(data)) if data[i]=='Z']
for zindex in range(len(zindexes)-181):
    o1=zindexes[zindex+181]-zindexes[zindex]+2+180+-1
    res.append(o1)
print(max(res))