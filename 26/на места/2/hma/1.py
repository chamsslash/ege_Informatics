f=open('Задание 1.txt')
z_c,r_c,m_c=map(int,f.readline().split())
res=[]
dalek_ryad_po_mestam=[r_c]*(m_c+1)
for i in f:
    ryad,mesto=map(int,i.split())
    dalek_ryad_po_mestam[mesto]=min(ryad-1,dalek_ryad_po_mestam[mesto])
for i1 in range(1,m_c+1-1):
    min_obsh_num=min(dalek_ryad_po_mestam[i1],dalek_ryad_po_mestam[i1+1])
    res.append([min_obsh_num,-(i1),-(i1+1)])
res.sort(reverse=True)
print(res[:5])
print(max(res))