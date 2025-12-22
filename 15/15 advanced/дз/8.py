def treug(n,m,k):
    return (n+m)>k and (n+k)>m and (k+m)>n
for A in range(10000,1,-1):
    for x in range(1,10000):
        # Для существования нужно, чтобы x+7>1006x+7>1006, то есть x>999          .
        if (not ( (treug(x,11,24) == (not (max(x,7) > 32))) and treug(x,A,7) ))==False:
            break
    else:
        print(A)