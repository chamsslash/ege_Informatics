q=list(range(8,17))
p=list(range(12,28))
a=list(range(1,100))
for x in range(1,100):
    if ((x in a)<=((x in p) and (not(x in q))))==False:
        a.remove(x)
print(a)
print(a[-1]-a[0])