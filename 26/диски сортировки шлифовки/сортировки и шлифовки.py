f=open('26.2.txt')
k=int(f.readline())
s_o=[[int(x.split()[0]),int(x.split()[1])] for x in f ]
s=[]
o=[]
for i in range(k):
    i1=i+1
    shl_t=s_o[i][0]
    okr_t=s_o[i][1]
    if shl_t<okr_t:
        s.append([shl_t,(i1)])
    else :
        o.append([okr_t,(i1)])
s.sort()
o.sort()

print(max(s),len(s)-1)