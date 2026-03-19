from itertools import product,permutations
cnter=0
for i1 in set(permutations('ВОРОТА',r=6)):
    i = ''.join(i1)
    if ('ОА' not in i) and ('АО' not in i) and ('ОО' not in i):
        cnter+=1
print(cnter)