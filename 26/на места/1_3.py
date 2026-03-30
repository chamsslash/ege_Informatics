from pprint import pformat

f=open('task1.txt')
zan_c,ryad_c,mest_c=map(int,f.readline().split())
aval=[]
ryads_po_mestam=[ryad_c]*(mest_c+1)
for zana in f:
    ryad,mesto=map(int,zana.split())
    ryads_po_mestam[mesto]=min(ryads_po_mestam[mesto],ryad-1)
for i in range(1,mest_c+-1):
    min_pair_place=min(ryads_po_mestam[i],ryads_po_mestam[i+1])
    aval.append([min_pair_place,i,i+1])
print(aval)
print(max(aval))
