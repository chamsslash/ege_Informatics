q=list(range(18,33))
p=list(range(5,21))
a=[i for i in range(1,10_000)]
for x in range(1,10_000):
    if (((x in a) <= (x in p)) or (x in q))==0:
        a.remove(x)
print(a)
print(a[-1]-a[0])