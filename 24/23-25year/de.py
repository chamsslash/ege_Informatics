f=open('task3.txt')
res=[]
data=f.readline().strip()
data='DE'+data+'DE'
data=data.replace('DE','Z')
z_indexes=[i for i in range(len(data)) if data[i]=='Z']
for zindex in range(len(z_indexes)-151):
    dlina=z_indexes[zindex+151]-z_indexes[zindex]-1+150+2
    res.append(dlina)
print(max(res))