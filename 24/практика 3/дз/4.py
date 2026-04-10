f=open('Задание 4.txt')
data=f.readline().strip()
res=[]
f_indexes=[i for i in range(len(data)) if data[i]=='F']
for findex in range(len(f_indexes)-752):
    o1=f_indexes[findex+752]-f_indexes[findex]+1
    res.append(o1)
print(min(res))