f=open('Задание 9.txt')
res=[]
data=f.readline().strip()
new_data=data.split('E')
for chunk in new_data:
    if chunk.count('C')<=300:
        res.append(len(chunk))
        continue
    chunk='C'+chunk+'C'
    cindexes=[i for i in range(len(chunk)) if chunk[i]=='C']
    for i in range(len(cindexes)-301):
        o1=cindexes[i+301]-cindexes[i]-1
        res.append(o1)
print(max(res))