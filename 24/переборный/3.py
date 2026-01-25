

#решение реплейсом
# repl="GHIJKLMNOPQRSTUVWXYZ"
# f=open("24_3.txt")
# data=f.readline()
# for rune in repl:
#     data=data.replace(rune," ")
    
# print(data)
# data=data.split()
# print(len(max(data,key=len)))

# решение переборным
from string import hexdigits
f=open("24_3.txt")
data=f.readline()
budd=data[0]
res=[]
for i in range(len(data)-1):
    if data[i] in hexdigits and data[i+1] in hexdigits:
        budd += data[i+1]
    else:
        budd = data[i+1]
    res.append(budd)

print(len(max(res, key=len)))
