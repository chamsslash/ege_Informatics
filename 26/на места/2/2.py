f=open('26_1.txt')
res=[]
z_c,r_c,m_c=map(int,f.readline().split())
data=[r_c]*(m_c+1)
for i in f:
    ryad,mesto=map(int,i.split())
    data[mesto]=min(data[mesto],ryad-1)
for y in range(1,len(data)-2):
    min_nim=min(data[y],data[y+1],data[y+2])
    res.append([min_nim,y,y+1,y+2])
res.sort(reverse=True)
print(max(res))
print(res[:5])