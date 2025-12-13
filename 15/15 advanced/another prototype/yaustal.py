a=list(range(3,81))
b=[x for x in range(2,177) if 177%x==0]
for y in range(1,10_000):
    c=[ i for i in range(2,y) if y %i ==0]
    if c:
        for x in range(1,10_000):
            if ((x in c) <= ((x in a) and (not(x in b))))==False :
                break
        else:
            print(y)