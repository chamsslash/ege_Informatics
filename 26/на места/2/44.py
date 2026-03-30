f=open('26_4.txt')
z_c,r_c,m_c=map(int,f.readline().split())
res=[]
ryadi_po_mestam=[[] for m in range(m_c+1)]
for visitor in f:
    ryad,mesto=map(int,visitor.split())
    ryadi_po_mestam[mesto].append(ryad)
for index_ryada in range(1,len(ryadi_po_mestam)):
    ryad_scheme=ryadi_po_mestam[index_ryada]
    ryad_scheme.append(0)
    ryad_scheme.append(r_c)
    ryad_scheme.sort(reverse=True)
    svoboda=0
    for index_place_ryada in range(len(ryad_scheme)-1):
        svoboda=ryad_scheme[index_place_ryada]-ryad_scheme[index_place_ryada+1]-1-1
        res.append([svoboda,-(ryad_scheme[index_place_ryada]-1),-(index_ryada)])

res.sort(reverse=True)
print(res[:5])
print(max(res))
