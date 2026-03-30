p=[i/10 for i in range(130,321)]
q=[i/10 for i in range(150,201)]
a=[i/10 for i in range(0,10_001)]
for x0 in range(0,10_001):
    x=x0/10
    if (((x in a) <= (x in p)) or (x in q))==0:
        a.remove(x)
print(a)
print(a[-1]-a[0])