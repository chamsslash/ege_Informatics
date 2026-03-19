from itertools import product,permutations
cnt=0
#
for i in permutations('0123456789AB',r=9):
    res=''.join(i)
    if ((res[0]!='0') and ((int(res,12)%2)!=0) and ((sum(res.count(o1) for o1 in '02468A'))==5)):
        cnt+=1
print(cnt)