f=open('Задание 3.txt')
data=f.readline().strip()
res=[]
o_inx=[ i for i in range(len(data)) if data[i]=='O']
for oindex in range(len(o_inx)-2906):
    o1=o_inx[oindex+2906]-o_inx[oindex]+1
    res.append(o1)
print((min(res)))