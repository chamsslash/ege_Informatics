r=[ i/10 for i in range(160,341)]
p=[i/10 for i in range(190,261)]
q=[i/10 for i in range(40,171)]
a=[]
for x in range(1,10_000):
    if (((x in a) or (x in p)) or ((x in q) <=(x in r)))==0:
        a.append(x)
print(a)