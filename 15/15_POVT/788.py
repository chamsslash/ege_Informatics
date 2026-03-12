p=list(range(27,131))
q=list(range(50,63))
r=list(range(38,95))
a=[]
for x in range(1,10_000):
    if (((x not in p) or (x in q)) or ((x not in a ) <= (x not in r)))==0:
        a.append(x)
print(a)
# 38- 50   62 94 это критические необходимые точки значит надо чтобы они все были включены,те a непрерывный отрезок который влючает это все
print(a[-1]-a[0])