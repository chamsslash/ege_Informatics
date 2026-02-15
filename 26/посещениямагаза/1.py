time=[0]*1441
izmena=[0]*1441

f=open("26.1.txt")
f.readline()
for pos in f:
    start,end=map(int,pos.split())
    izmena[start]+=1
    izmena[end]-=1
cnt=0
for i in range(1440):
    cnt+=izmena[i]
    time[i]=cnt
maxi=max(time)
o=[i for i in range(1440) if time[i] ==maxi]
print(o,maxi)
# for pos in f:
#     start,end=map(int,pos.split())
# потому что при end он как бы вышел уже
#     for i in range(start,end):
#         time[i]+=1
# maxi=max(time)
# o=[i for i in range(1440) if time[i] ==maxi]
# print(o,maxi)