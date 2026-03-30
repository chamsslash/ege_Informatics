from  itertools import *
cnt=0
for i in product("01234567",repeat=4):
    o1=''.join(i)
    if (all((o1[0]!=f'{ch}' for ch in '0246')) and ((o1[-1] != '0') and (o1[-1] != '7') and (o1[0]!='0') and (o1.count('5')<=1))) :
        cnt+=1
print(cnt)

