p=list(range(10,27+1))
q=list(range(25,44))
a=[]
for x in range(0,10_001):
    if (((x in p ) and (not(x in q))) <= (x in a))==0:
        a.append(x)
print(a)
# 15