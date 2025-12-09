q=list(range(17,92))
p=list(range(10,48))
a=[]
for x in range(1,100):
    if (((x in p) and (x in q ))<= (x in a))==False:
        a.append(x)
print(a)
# 30