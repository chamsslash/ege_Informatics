p=list(range(25,65))
q=list(range(40,116))
a=[]
for x in range(0,10_000):
    if ((x in p)<=(((x in q) and not(x in a)) <= (not(x in p))))==0:
        a.append(x)
print(a)
#24