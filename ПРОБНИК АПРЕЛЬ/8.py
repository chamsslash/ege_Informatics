from itertools import *
res=[]
num=0
for i in product('СТРЕЛА',repeat=5):
    num+=1
    n=''.join(i)
    if ((num%2)==0) and (n[0] not in ['А','С','Т'] and (n.count('Л')) and ('ЛЛ' not in n)):
        res.append(num)
print(max(res))