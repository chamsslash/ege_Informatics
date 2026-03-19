from itertools import product,permutations
cnt=0
for i in product('0123456',repeat=4):
    res=''.join(i)
    if ((res[0]!='0')and(res.count('5')==1) and all((f"2{ch}" not in res) for ch in '135') and all((f"{ch}2" not in res) for ch in '135')):
        cnt+=1
print(cnt)
