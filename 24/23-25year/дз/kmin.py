f=open('Задание 1.txt')
data=f.readline().strip()
res=[]
k_indexes=[i for i in range(len(data)) if data[i]=='K']
for kindex in range(len(k_indexes)-309):
    dlina=k_indexes[kindex+309]-k_indexes[kindex]+1
    res.append(dlina)
print(res)
print(min(res))