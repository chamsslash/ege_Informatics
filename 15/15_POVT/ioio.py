q=[i/10 for i in range(390,711)]
p=[ i/10 for i in range(150,991)]
a=[]
for x in range(0,2000):
    x=x/10
    if ((x in p) <= (((x in q) and (x in p)) or ((x not in q)<=(x in a))))==0:
        a.append(x)
print(a[-1]-a[0])