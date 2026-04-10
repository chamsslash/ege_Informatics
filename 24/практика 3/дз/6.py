f=open('Задание 6.txt')
data=f.readline().strip()
data='N'+data+'N'
nIndexes=[i for i in range(len(data)) if data[i]=='N']
res=[]
for i in range(len(nIndexes)-160):
    o1=nIndexes[i+160]-nIndexes[i]-1
    res.append(o1)
print(max(res))