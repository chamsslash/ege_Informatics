q=list(range(12,23))
p=list(range(3,13))
a=list(range(1,100))
for x in range(1,100):
    if( ((x in a )<=(x in p)) or (x in q))==False:
        a.remove(x)
print(a)
print(a[-1]-a[0])