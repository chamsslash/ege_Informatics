from  itertools import *
c=0
for i in product('ГЕПАРД',repeat=5):
    o1=''.join(i)
    if (o1.count('Г')==1) and (o1[0]!= 'А') and (o1[-1]!='Е'):
        print(o1)
        c+=1
print(c)