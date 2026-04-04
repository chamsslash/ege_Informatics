f=open('Задание 8.txt')
data=f.readline().strip().replace('RO','Z')
data='Z'+data+'Z'
res=[]
zindexes=[i for i in range(len(data)) if data[i]=='Z']
for i in range(len(zindexes)-359):
    o1=zindexes[i+359]-zindexes[i]+2-1+358
    res.append(o1)
print(max(res))