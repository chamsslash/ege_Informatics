q=list(range(10,56))
p=list(range(4,21))
a=[]
for x in range(1,10_000):
    if (x in a) or ((x not in p)<= (x not in q))==0:
        a.append(x)
print(a)
# тк это мин список a то в нем базовый минимум без которого уже будет фолс поэтому берем его полностью