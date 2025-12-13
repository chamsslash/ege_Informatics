q=[x/10 for x in range(180,421)]
p=[x/10 for x in range(100,211)]
a=[x/10 for x in range(10,1000)]
for x0 in range(10,1000):
    x=x0/10
    if (((x in q)<=(x in p))<=(not(x in a)))==False:
        a.remove(x)
print(a)
