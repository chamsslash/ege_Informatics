from itertools import *
num=0
res=[]
for i in sorted(product('АПРЕЛЬ',repeat=5)):
    num+=1
    r=''.join(i)
    if ((num%2==0) and (r[0] not in 'ЬР') and (r.count('Л')>=2)):
        res.append(num)
print(max(res))