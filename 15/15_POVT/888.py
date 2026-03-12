q=list(range(18,31))
p=list(range(5,17))
a=[]
for x in range(1,10_000):
    if (((x in p) or (x in q)) <= (x in a))==0:
        a.append(x)
print(a)
print(a[-1]-a[0])