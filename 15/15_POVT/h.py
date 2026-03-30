q=list(range(21,58))
p=list(range(3,39))
a=[i for i in range(1,10_000)]
for x in range(1,10_000):
    if  (( (x in q)<= (x in p)) <= (x not in a))==0:
        a.remove(x)
print(a)
# 38 --  57
# 57-38=19