f=open('24.5.txt')
res=[]
data=f.readline().strip()
aindexes=[ i for i in range(len(data)) if data[i] == 'A']
for i in range( len(aindexes)-499 ):
    o1=aindexes[i+499]-aindexes[i]+1
    res.append(o1)
print(min(res))