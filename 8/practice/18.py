from itertools import *
cnt1=0
for i in product('смарт',repeat=6):
    w=''.join(i)
    if (w.count('р')<=1) and (w[0]!='р') and (w[-1]!='р') and ('рт' not in w) and ('тр' not in w):
        cnt1 += 1
print(cnt1)