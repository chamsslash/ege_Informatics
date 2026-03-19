from itertools import permutations
cnt=0
for i in set(permutations('НАГЛЕЖ',r=4)):
    pod=''.join(i)
    if (all((f'{gl}{gl1}'not in pod) for gl in 'АЕ' for gl1 in 'АЕ')):
        cnt+=1

print(cnt)
