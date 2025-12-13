q=[x/10 for x in range(100,200)]
p=[x/10 for x in range(250,301)]
a=[]
for x0 in range( 10,1000):
    x=x0/10
    if (not((x in q) or (x in p))<=(x in a)):
        a.append(x)
print(a)