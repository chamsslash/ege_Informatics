p=[i/10 for i in range(110,281)]
q=[i/10 for i in range(210,421)]
a=[x/10 for x in range(0,10_001)]
for x in range(0,10_001):
    x=x/10
    if (((x in p) == (x in q)) <= (x not in a))==0:
        a.remove(x)
print(a)
print(len(a)/10)