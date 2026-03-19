from itertools import product,permutations
from string import printable
cnt=0
alph=printable[:21]
def to21(n):
    res=''
    while n:
        res+=alph[n%26]
        n//=26
    return res[::-1]
for i in product(alph,repeat=6):
    pod=''.join(i)
    if ((pod.count('6')==1) and ((sum(pod.count(o1) for o1 in alph[12:]))>=3) and (pod[0]!='0')):
        cnt+=1
print(cnt)