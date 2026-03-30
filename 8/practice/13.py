from itertools import product,permutations
cnt=0
for i in product('ПАЛЬТО',repeat=5):
    gpt=''.join(i)
    if ((gpt.count('О')<=2 )and (gpt[0]!='О') and (gpt[-1]!='О') and ('ЛО' not in gpt) and 'ОЛ' not in gpt):

        cnt+=1
print(cnt)
