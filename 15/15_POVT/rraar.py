q=[i/10 for i in range(100,301)]
p=[i/10 for i in range(50,151)]
a=[i/10 for i in range(0,10_001)]
for x in range(0,10_001):
    x=x/10
    if (((x in a) <= (x in p) ) or (x in q ))==0:
        a.remove(x)
print(a)
print(len(a))
print(a[-1]-a[0])