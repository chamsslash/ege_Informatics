import math
i=700_001
res=[]
while len(res)!=5:
    # упрощение ведь минимальнй делитель будет первым и максимальный будет в паре с ним
    M = 0
    for ch1 in range(2,int(math.sqrt(i))+1):
        if i%ch1==0:
            M = ch1 + (i // ch1)
            break
    if str(M)[-1]=="4":
         res.append([i,M])
    i+=1
print(res[-1])