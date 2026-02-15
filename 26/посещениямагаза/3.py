f=open("1.txt")
f.readline()
sec=[0]*1441
for i in f:
    start,end=map(int,i.split())
    for i1 in range(start,end):
        sec[i1]+=1
maxi=max(sec)
o=[i for i in range(1440) if sec[i]==maxi]
print(o,maxi)
# f=o.pen("1.txt")
# f.readline()
# sec=[0]*1441
# izm=[0]*1441
# for i in f:
#     start,end=map(int,i.split())
#     izm[start]+=1
#     izm[end]-=1
# c=0
# for i in range(1441):
#     c+=izm[i]
#     sec[i]=c
# maxi=max(sec)
# o=[i for i in range(1440) if sec[i]==maxi]
# print(o,maxi)

