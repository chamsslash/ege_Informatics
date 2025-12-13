p=[x/10 for x in range(100,350+1)]
q=[x/10 for x in range(160,580+1)]
a=[]
for x0 in range(1,1000):
    x=x0/10
    if ((x in p)<=((((x in q ) and (not(x in a)))<=(not(x in p)))))==False:
        a.append(x)
print(a)
# 16-35