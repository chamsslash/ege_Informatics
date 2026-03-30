f=open('Задание 4.txt')
res=[]
z,r,m=map(int,f.readline().split())
ryadi_po_mestam=[[] for i in range(m+1)]
for i in f:
    r,m=map(int,i.split())
    ryadi_po_mestam[m].append(r)
for ryad_index in range(1,len(ryadi_po_mestam)):
    ryad_scheme=ryadi_po_mestam[ryad_index]
    ryad_scheme.append(0)
    ryad_scheme.append(r)
    ryad_scheme.sort(reverse=True)
    svo=0
    for index_zanatogo in range(len(ryad_scheme)-1):
        svo=ryad_scheme[index_zanatogo]-ryad_scheme[index_zanatogo+1]-1-1
        res.append([svo,-(ryad_scheme[index_zanatogo]-1),-ryad_index])
res.sort(reverse=True)
print(res[:5])
print(max(res))