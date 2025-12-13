p=[x/10 for x in range(250,551)]
q=[x/10 for x in range(130,301)]
def Del(n,m):
     return  n%m==0
a=[]
for x0 in range(10,1000):
    x=x0/10
    if (((x in p)<=(Del(x,14)or (x in q)))<=(x in a)):
        a.append(x)
print(a)
