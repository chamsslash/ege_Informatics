p=[x/10 for x in range(110,281)]
q=[x/10 for x in range(210,421)]
a=[x/10 for x in range(10,1000)]
for x0 in range(10,1000):
    x=x0/10
    if (((x in p )==(x in q)) <= (not(x in a)))==False:
        a.remove(x)
print(a)