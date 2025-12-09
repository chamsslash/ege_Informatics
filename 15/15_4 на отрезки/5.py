p= list(range(13,33))
q =list(range(15,21))
a=list(range(1,100))
for x in range(1,100):
    if ((x in a)<=(x in p) or (x in q))==False:
        a.remove(x)
print(a)