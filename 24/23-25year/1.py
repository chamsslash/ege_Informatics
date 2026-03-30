f=open('task1.txt')
res=[]
data=f.readline().strip()
# data='T'+data+'T'
t_inxes=[i for i in range(len(data)) if data[i]==('T')]
for t_index in range(len(t_inxes)-209):
    dlina=t_inxes[t_index+209]-t_inxes[t_index]+1
    res.append(dlina)
print(min(res))