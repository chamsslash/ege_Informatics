f=open('Задание 4.txt')
data=f.readline().strip().replace('RO','Z')
data="Z"+data+'Z'
z_indexes=[i for i in range(len(data)) if data[i]=='Z']
res=[]
for zindex in range(len(z_indexes)-359):
    dlina=z_indexes[zindex+359]-z_indexes[zindex]+2-1+358
    res.append(dlina)
print(max(res))