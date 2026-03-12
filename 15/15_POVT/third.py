p=list(range(7,16))
q=list(range(20,39))
a=[i for i in range(1,10_000)]
for x in range(1,10_000):
    if (((x not in p) <= (x in q)) or (x not in a))==0:
        a.remove(x)
print(a)
# 7 15    and   20 38
# 38-20=18