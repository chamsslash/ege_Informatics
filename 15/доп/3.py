q=[18,41]
p=[9,17]
a=[]
for x in range(1,100):
    if (x in p) or ((x in q) <= (x in a))==False:
        a.append(x)
print(a)
print(a[-1]-a[0])