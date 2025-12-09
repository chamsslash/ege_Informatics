p=list(range(11,29))
q=list(range(21,43))
# просят максимум
a= list(range(1,100))
for x in range(1,100):
    if (((x in p)<=(x in q) )<= (not(x in a)))==False:
        a.remove(x)
print(a[-1]-a[0]+1)