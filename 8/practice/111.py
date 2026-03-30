from itertools import product
cnt=0
for i in product('123456',repeat=4):
    w=''.join(i)
    if (( w.count('4')==1) and (sum(w.count(ch) for ch in '246')<= sum(w.count(nc) for nc in '135'))):
        cnt+=1
print(cnt)