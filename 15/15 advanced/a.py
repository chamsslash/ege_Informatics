q=[x/10 for x in range(100,301)]
p=[x/10 for x in range(50,151)]
a=[x/10 for x in range(10,1000)]
for x0 in range(10,1000):
    x=x0/10
    if (((x in a)<=(x in p)) or (x in q))==False:
        a.remove(x)
print(a)