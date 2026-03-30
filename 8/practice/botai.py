from itertools import permutations,product
cnt=0
for i in product("БОТАЙ",repeat=3):
    pod='.'.join(i)
    if ((pod.count('Б'))==1) and (pod[0]!='А') and (pod[-1]!='Й'):
        cnt+=1
print(cnt)