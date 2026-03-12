p=list(range(20,151))
q=list(range(40,101))
r=list(range(30,121))
s=list(range(10,81))
t=list(range(60,201))
u=list(range(90,171))
a=[]
for x in range(0,10_01):
    if (((x in p) or (x in q)) or ((x not in a)  <= ((x in r ) and (x in s) or (x in t) and (x in u))      ))==0:
        a.append(x)
print(a)