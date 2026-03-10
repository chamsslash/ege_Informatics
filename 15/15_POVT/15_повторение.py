p=[i/10 for i in range(30,181)]
q=[i/10 for i in range(110,241)]
A=[]
for x in range(1,10000):
    x=x/10
    if (((x in p) and (x in q)) <= (x in A))==0:
         A.append(x)

print(A)
print(A[-1]-A[0])