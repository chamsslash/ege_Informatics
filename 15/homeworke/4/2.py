q=list(range(12,30))
p=list(range(5,41))
a=[]
for x in range(1,100):
    if (((x in a ) and (x in p) ) or (not(x in q)))==False:
        a.append(x)
print(a)
print(a[-1]-a[0])