r=list(range(12,31))
q=list(range(8,16))
p=list(range(10,21))
a=[]
for x in range(1,10_000):
    if (((x in a) or (x in p)) or ((x in q) <= (x in p)))==0:
        a.append(x)
print(a)
