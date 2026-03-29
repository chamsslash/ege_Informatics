f=open('Задание 2.txt')
z,r,m=map(int,f.readline().split())
res=[]
dalekie_po_mestam=[r]*(m+1)
for i in f:
    ry,me=map(int,i.split())
    dalekie_po_mestam[me]=min(dalekie_po_mestam[me],ry-1)
for i1 in range(1,len(dalekie_po_mestam)-2):
    min_num=min(dalekie_po_mestam[i1],dalekie_po_mestam[i1+2],dalekie_po_mestam[i1+1])
    res.append([min_num,i1,i1+1,i1+2])
res.sort(reverse=True)
print(max(res))
print(res[:5])
