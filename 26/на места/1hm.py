f=open('Задание 1.txt')
res=[]
zanat_c,ryad_c,mesta_c=map(int,f.readline().split())
ryadi_po_mestam=[ryad_c]*(mesta_c+1)
for zanyal in f:
    ryad,mesto=map(int,zanyal.split())
    ryadi_po_mestam[mesto]=min(ryadi_po_mestam[mesto],ryad-1)
print(ryadi_po_mestam)
#
# for num_mesta in range(1,len(ryadi_po_mestam)-1):
#     min_ryad_dla_pari=min(ryadi_po_mestam[num_mesta],ryadi_po_mestam[num_mesta+1])
#     res.append([min_ryad_dla_pari,num_mesta,num_mesta+1])
# res.sort(reverse=True)
# print(res)
# print(max(res))