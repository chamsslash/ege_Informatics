cnt=0
from itertools import product
for i in product('01234567',repeat=5):
    x = ''.join(i)
    if ((x[0] not in '01357')  and (x[-1] not in '26') and (x.count('7')<=2)):
        cnt+=1
print(cnt)