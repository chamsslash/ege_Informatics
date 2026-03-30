f=open('task2.txt')
res=[]
data=f.readline().strip()
data='M'+data+'M'
M_Indexes=[i for i in range(len(data)) if data[i] =='M']
for mindex in  range(len(M_Indexes)-101):
    dlina=M_Indexes[mindex+101]-M_Indexes[mindex]-1
    res.append(dlina)
print(max(res))