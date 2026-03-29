f=open('Задание 3.txt')
data=f.readline().strip().replace('XZ','O')
res=[]
o_indexes=[i for i in range(len(data)) if data[i]=='O']
for oindex in range(len(o_indexes)-28):
    dlina=o_indexes[oindex+28]-o_indexes[oindex]+1+29
    res.append(dlina)
print(min(res))