from itertools import product
cnt=0
alpha='0123456'
for i in product(alpha,repeat=4):
    w=''.join(i)
    if ((w[0]!='0') and (w.count('5')==1) and all(( (f'2{nc}' not in w) and  ((f'{nc}2') not in w) ) for nc in '135')):
        cnt+=1
print(cnt)