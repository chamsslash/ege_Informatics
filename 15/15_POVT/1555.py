p=[i/10 for i in range(130,331)]
q=[i/10 for i in range(220,441)]
a=[]
for x in range(1,10_000):
    x=x/10
    if ((not(x in a)) <= (((x in p) and (x in q)) <= (x in a)))==0:
        a.append(x)
print(a)
print(a[-1]-a[0])