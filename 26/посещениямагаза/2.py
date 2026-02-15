# f=open('26.2.txt')
# sec=[0]*86400
# f.readline()
# for i in f:
#     start,end=map(int,i.split())
#     for index in range(start,end):
#         sec[index]+=1
# maxi=max(sec[8*60*60:14*60*60])
# o=[i for i in range(86400) if sec[i]==maxi]
# print(maxi,len(o))
# второй способ
f=open('26.2.txt')
sec=[0]*86401
izm=[0]*86401
f.readline()
for i in f:
    start,end=map(int,i.split())
    izm[start]+=1
    izm[end]-=1
cnt=0
for i1 in range(86401):
    cnt+=izm[i1]
    sec[i1]=cnt
maxi=max(sec)

o=[i for i in range(86400) if sec[i]==maxi]
print(maxi,len(o))