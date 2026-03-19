f=open('Задание 2.txt')
zan_c,ryad_c,mesta_c=map(int,f.readline().split())
res=[]
zanyatie_ryadi_po_mestam=[[] for _ in range(mesta_c+1)]
for visit in f:
    ryad,mesto=map(int,visit.split())
    zanyatie_ryadi_po_mestam[mesto].append(ryad)
for  mesto_scheme in zanyatie_ryadi_po_mestam[1:]:
    mesto_scheme.append(ryad_c+1)
    mesto_scheme.append(0)
    mesto_scheme.sort(reverse=True)
    for zanyatoe_mesto in range(len(mesto_scheme)-1):
        rasst=mesto_scheme[zanyatoe_mesto]-mesto_scheme[zanyatoe_mesto+1]-1-1
        res.append([rasst,mesto_scheme[zanyatoe_mesto]-1])
res.sort(reverse=True)
print(res)
print(max(res))
