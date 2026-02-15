# f=open("2.txt")
# f.readline()
# sec=[0]*86401
# for i in f:
#     start,end=map(int,i.split())
#     for i1 in range(start,end):
#         sec[i1]+=1
# maxi=max(sec[8*60*60:14*60*60+1])
# o=[sec[8*60*60:14*60*60+1].count(maxi)]
# print(maxi,o)

f=open("2.txt")
f.readline()
sec=[0]*86401
izm=[0]*86401
for i in f:
    start,end=map(int,i.split())
    izm[start]+=1
    izm[end]-=1
c=0
for i in range(86400):
    c+=izm[i]
    sec[i]=c
maxi=max(sec[8*60*60:14*60*60+1])
o=[sec[8*60*60:14*60*60+1].count(maxi)]
print(maxi,o)
