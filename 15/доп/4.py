q=[i/10 for i in range(260,510+1)]
p=[i/10 for i in range(100,351)]
a=[]
for x0 in range(1,10000):
    x=x0/10
    if (((x in p)<=(not(x in q)))or(x in a))==0:
        a.append(x)
print(len(a)-1)