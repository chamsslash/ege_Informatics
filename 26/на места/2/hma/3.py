f=open('Задание 3.txt')
res=[]
z,r,m=map(int,f.readline().split())
ryadi_po_mestam=[[] for i in range(m+1)]
for i in f:
    ry,me=map(int,i.split())
    ryadi_po_mestam[me].append(ry)
for index_ryada in range(1,len(ryadi_po_mestam)):
    ryad_scheme=ryadi_po_mestam[index_ryada]
    ryad_scheme.append(0)
    ryad_scheme.append(r)
    ryad_scheme.sort(reverse=True)
    svo=0
    for index_zanatogo_mesta in range(len(ryad_scheme)-1):
        svo=ryad_scheme[index_zanatogo_mesta]-ryad_scheme[index_zanatogo_mesta+1]-1-1
        res.append([svo,-(ryad_scheme[index_zanatogo_mesta]-1),-index_ryada])
res.sort(reverse=True)
print(res[:5])
print(max(res))



