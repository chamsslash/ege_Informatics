from  itertools import product
cnt=0
for i in product("123456",repeat=5):
    res=''.join(i)
    c_chet=0
    c_nechet=0
    for digit in res:
        if int(digit)%2==0:
            c_chet+=1
        else:
            c_nechet+=1
    if res.count('3')==1 and c_chet<=c_nechet:
        print(i)
        cnt+=1
print(cnt)
