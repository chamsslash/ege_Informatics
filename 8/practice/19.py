from itertools import product,permutations
cnt=0
for i in product('01234567',repeat=5):
    r=''.join(i)
    for i in r:
        if i in '1357':
            r=r.replace(i,'*')
    if (r[0]!= '0')and  (r.count('4')==2) and ("*4" not in r) and('4*' not in r):
        cnt+=1
print(cnt)
