p = list(range(13,34))
q=list(range(22,45))
a=[]
for x in range(1,100):
    if ((not(x in a)) <= (((x in p) and (x in q))<=(x in a)))==False:
        a.append(x)
print(a[-1]-a[0])