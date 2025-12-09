p=list(range(16,60))
q=list(range(27,72))
a=[]
for x in range(1,100):
    if ((not(x in a))<=((x in p) <= (not(x in q))))==False:
        a.append(x)
print(a)
print(a[-1]-a[0])