from string import printable
from itertools import permutations
alpha=printable[:12]
cnt=0
for i in permutations(alpha,r=9):
    w=''.join(i)
    if (( w[0] != '0') and ((int(w,12)%2)!=0) and (sum(w.count(ch) for ch in '02468a')==5)):
        cnt+=1
print(cnt)