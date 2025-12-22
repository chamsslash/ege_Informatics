def ugolok(n,m,k):
    return n+m+k==180
for a in range(1,10_00):
    for x in range(1,10_00):
        if (ugolok(47,a,x+40)==(ugolok(a,x,45)and(not(a+30<156))))==False:
            break
    else:
        print(a)