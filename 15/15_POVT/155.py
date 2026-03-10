p=[i/10 for i in range(160,591)]
q=[i/10 for i in range(270,719)]
a=[]
for x in range(1,10_000):
    x=x/10
    if ((not(x in a)) <= ((x in p) <= (not(x in q))))==0:
        a.append(x)
print(a)
print(a[-1]-a[0])