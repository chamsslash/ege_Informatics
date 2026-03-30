from itertools import product
from string import printable
cnt=0
alpha=printable[:21]
for i in product(alpha,repeat=6):
    w=''.join(i)
    if (w[0]!='0') and (w.count('6')==1) and sum(w.count(char) for char in printable[12:21])>=3:
        cnt+=1
print(cnt)