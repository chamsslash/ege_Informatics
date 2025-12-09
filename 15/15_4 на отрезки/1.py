p=list(range(3,19))
q=list(range(11   ,25))
a=[]
for x in range(1,100):
    if  (((x in p) and (x in q)) <= (x in a))==False:
        a.append(x)
print(a)