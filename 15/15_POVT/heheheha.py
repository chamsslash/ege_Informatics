q=list(range(33,89))
p=list(range(10,50))
a=[i for i in range(1,10000)]
for x in range(1,10_000):
    if (((x in p)<=(x not in q)) <= (x not in a))==0:
        a.remove(x)
print(a)
print(a[-1]-a[0])