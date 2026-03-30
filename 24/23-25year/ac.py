f=open('task4.txt')
data = f.readline().strip().replace('AC','Z')
z_indexes=[i for i in range(len(data)) if data[i]=='Z' ]
res=[]
for zindex in range(len(z_indexes)-24):
    dlina=z_indexes[zindex+24]-z_indexes[zindex]+1+25
    res.append(dlina)
print(min(res))