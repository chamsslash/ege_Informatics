f=open('26_3.txt')
res=[]
z_c,r_c,m_c=map(int,f.readline().split())

ryadi_po_mestam=[[]for i in range(m_c+1)]
for i in f:
    ryad,mest=map(int,i.split())
    ryadi_po_mestam[mest].append(ryad)
for ik in range( 1,len(ryadi_po_mestam)):
    zapolnenit_ryada=ryadi_po_mestam[ik]
    zapolnenit_ryada.append(0)
    zapolnenit_ryada.append(r_c)
    zapolnenit_ryada.sort(reverse=True)
    svob=0
    for i in range(len(zapolnenit_ryada)-1):
            svob=zapolnenit_ryada[i]-zapolnenit_ryada[i+1]-1-1
            res.append([svob,-(zapolnenit_ryada[i]-1),-(ik)])
res.sort(reverse=True)
print(res[:5])
print(max(res))

