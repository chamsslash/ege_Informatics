f=open('Задание 2.txt')
data=f.readline().strip()
data='O'+data+'O'
o_indexes=[i for i in range(len(data)) if data[i]=='O']
res=[]
for i in range(len(o_indexes)-151):
    dlina=o_indexes[i+151]-o_indexes[i]-1
    res.append(dlina)
print(max(res))
